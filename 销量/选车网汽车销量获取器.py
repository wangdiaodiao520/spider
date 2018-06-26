from tkinter import *
import tkinter.messagebox as messagebox
import urllib.request
import re
import time
import xlrd
import pymongo
from xcxlpc import *

#给大佬写的从选车网查销量的GUI
class Application(Frame):
    #连接数据库
    client=pymongo.MongoClient('localhost')
    db=client['汽车销量数据']
    #初始化界面
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    #交互界面设置
    def createWidgets(self):
        self.addressInput = Entry(self)
        self.startInput = Entry(self)
        self.endInput = Entry(self)
        self.addressInput.pack()
        self.startInput.pack()
        self.endInput.pack()
        self.alertButton = Button(self, text='爬取', command=self.spider)
        self.alertButton.pack()

    def spider(self):
        #输入爬取汽车的文件，查询时间始末
        address = self.addressInput.get() or '地址错误'
        start=self.startInput.get() or '开始时间错误'
        end=self.endInput.get() or '结束时间错误'
        #开始提示
        messagebox.showinfo('Message', '爬取开始')
        #没啥用的一堆垃圾代码
        chosetime='--'+start+'--'+end
        base_url='http://www.chooseauto.com.cn/public/ajax/getdata_xl_chart2.asp?t=0--'
        #从汽车表格中提取链接信息，组成请求链接   ps：选车网面对会员，经测试，发现这种方法可以绕过会员限制，手动划重点
        book=xlrd.open_workbook(address)
        sheet=book.sheets()[0]
        f=lambda x:sheet.col_values(x)
        pp=f(0)
        cs=f(1)
        cx=f(2)
        gb=f(3)
        jibie=f(4)
        leibie=f(5)
        f_e=lambda x : x.encode('unicode-escape').decode().replace('\\','%')
        for i in range(len(pp)):
            main(
                x=f_e(pp[i]),
                y=f_e(cs[i]),
                z=f_e(cx[i]),
                m=f_e(gb[i]),
                n=f_e(jibie[i]),
                p=f_e(leibie[i])
                )
        url = base_url+'pp|'+x+'$sccj|'+y+'$pm|'+z+'$gb|'+m+'$CHEJIBIE|'+n+'$CX|'+p+chosetime
        #解析请求的到的json
        html=get_page(url)
        for item in get_data(html):
            save_data(item)
        #测试了下，3秒才是真男人，网站那么水，几条数据就限制，一共要的也不多，懒得用代理了
        time.sleep(3)
            
        
#去吧，皮皮虾
app = Application()

app.master.title('爬取销量')

app.mainloop()
