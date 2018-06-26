# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class CarItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    send_time=Field()
    make=Field()
    back_time=Field()
    num=Field()
    model=Field()
    bad=Field()
    mybe=Field()
    repair=Field()
    change=Field()
    tousu=Field()