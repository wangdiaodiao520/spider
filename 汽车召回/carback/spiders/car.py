# -*- coding: utf-8 -*-
from scrapy import Spider,Request
import requests
from carback.items import CarItem

class CarSpider(Spider):
    name = 'car'
    allowed_domains = ['www.qiche365.org.cn']
    start_urls = ['http://www.qiche365.org.cn/index.php?m=all&c=index&a=recall_list']

    def parse(self, response):
        base_url='http://www.qiche365.org.cn'
        links=response.xpath('//span[@class="ina_zh"]/a/@href').extract()
        for i in range(len(links)):
            link=base_url+links[i]
            yield Request(url=link,callback=self.page_parse)

        next=response.xpath('//div[@class="ina_fanye"]/a/@href').extract()[7]
        yield Request(url=next,callback=self.parse)

    def page_parse(self,response):
        long = response.xpath('//div[@class="ina_table"]/table/tr')
        item = CarItem()

        item['send_time'] = response.xpath('//div[@class="ina_table"]/table/tr[1]/td/text()').extract_first()
        item['make'] = response.xpath('//div[@class="ina_table"]/table/tr[2]/td[2]/text()').extract_first()
        item['back_time'] = response.xpath('//div[@class="ina_table"]/table/tr[3]/td[2]/text()').extract_first()
        item['num'] = response.xpath('//div[@class="ina_table"]/table/tr[4]/td[2]/text()').extract_first()
        #for x in range(6, len(long) - 8):
        item['model'] =[response.xpath('//div[@class="ina_table"]/table/tr[$val]/td/p/text()', val=x).extract() for x in range(6, len(long) - 8)]
        item['bad'] = response.xpath('//div[@class="ina_table"]/table/tr[$val]/td[2]/text()', val=len(long) - 8).extract_first()
        item['mybe'] = response.xpath('//div[@class="ina_table"]/table/tr[$val]/td[2]/text()', val=len(long) - 7).extract_first()
        item['repair'] = response.xpath('//div[@class="ina_table"]/table/tr[$val]/td[2]/text()', val=len(long) - 6).extract_first()
        item['change'] = response.xpath('//div[@class="ina_table"]/table/tr[$val]/td[2]/text()', val=len(long) - 5).extract_first()
        item['tousu'] = response.xpath('//div[@class="ina_table"]/table/tr[$val]/td[2]/text()', val=len(long) - 4).extract_first()
        yield item





















