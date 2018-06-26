from tkinter import *
import tkinter.messagebox as messagebox
import urllib.request
import re
import time
import xlrd
import pymongo
from xcxlpc import *

class Application(Frame):

    client=pymongo.MongoClient('localhost')
    db=client['汽车销量数据']
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

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
        address = self.addressInput.get() or '地址错误'
        start=self.startInput.get() or '开始时间错误'
        end=self.endInput.get() or '结束时间错误'
        messagebox.showinfo('Message', '爬取开始')

        chosetime='--'+start+'--'+end
        base_url='http://www.chooseauto.com.cn/public/ajax/getdata_xl_chart2.asp?t=0--'

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

        html=get_page(url)
        for item in get_data(html):
            save_data(item)
        time.sleep(3)
            
        

app = Application()

app.master.title('爬取销量')

app.mainloop()
