# 首先，导入所需要的相关模块。
import requests
from bs4 import BeautifulSoup
from urllib.request import quote
import tkinter
from tkinter import Tk,Button,Entry,Label,Text,END

# 接着，请求爬取网页。
def crawl(word):
    # -------------加了requests headers
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
    # params = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    # 'Accept - Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,es-US;q=0.6,es;q=0.5',
    # 'Connection': 'keep-alive',
    # 'DNT': '1',
    # 'Host': 'lajifenleiapp.com',
    # 'Referer':'https://lajifenleiapp.com/',
    # 'Upgrade - Insecure - Requests': '1',
    # 'User - Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36',
    # }

    url = "http://lajifenleiapp.com/sk/"+quote(word)
    res0 = requests.get(url,headers=headers)
    res = BeautifulSoup(res0.text,'html.parser')
    a=res.find_all(class_="col-md-12")#23
    # print(a[0].text)
    # print('-'*75)


# 将爬取得数据进行清洗筛选，从中选取自己需要的数据。
    if a[0].text !='未查到完全匹配字段。':
        b = res.find_all("li")
        '''
        for i in range(10):
            print(i, '\n',a[i])
        '''
        # ------------严重错误!!!!!!!!!, IndexError: list index out of range, 从4,5,6,7,8改成了3,4,5,6,7
        # print(a[0].text,a[1].text,a[3].text,a[4].text,a[5].text,a[6].text,a[7].text)
        return "相似物品:\n"+a[0].text.replace("\n"," ").replace("相关查询：","").strip()+"\n\n"+''.join(a[1].text.split())+"\n\n"+a[3].text+"\n"+a[4].text+"\n\n"+a[5].text+"\n"+a[6].text+"\n\n"+a[7].text+"\n"+b[0].text+"\n"+b[1].text
    else:
        return word+"可不是什么垃圾，哼，请重新搜索"

# 最后，对垃圾分类器界面端的大小、颜色等进行设计。
win = tkinter.Tk()  #生成win主窗口
win.title("垃圾分拣查询器")  #修改框体的名字
win.geometry("400x400+200+50")  #指定主框体大小   
win.minsize(310,470)  
win.maxsize(310,470)
result_text1 = Text(win,background = 'azure')  #文本框（多行）
result_text1.place(x = 10,y = 5,width = 285,height = 70)  #place组件可以直接使用坐标来放置组件
# x:组件左上角的x坐标；y:组件左上角的y坐标；width:组件的宽度；height:组件的高度
# result_text1.bind("<Key-Return>","submit1")
# 对于按钮组件、菜单组件等可以在创建组件时通过command参数指定其事件处理函数。方法为bind
# 事件关联 bind(sequence,func,add)  # 这一步并不产生任何作用，是文本框的作用
title_label = Label(win, text=u'垃圾分类查询结果：')  #生成标签
title_label.place(x=10, y=100)
# 翻译结果
result_text = Text(win, background='light cyan')
result_text.place(x=10, y=120, width=285, height=325)
def submit1():
    content = result_text1.get(0.0, END).strip().replace("\n", " ") #可用set和get方法进行传值和取值
    # 把这个值传送给服务器进行翻译
    result = crawl(content)
    result_text.delete(0.0, END)
    result_text.insert(END, result)
def submit():
    content = result_text1.get(0.0,END).strip().replace("\n"," ")
    result = crawl(content)
    result_text.delete(0.0, END)
    result_text.insert(END, result)
def clean():
    result_text1.delete(0.0,END)
    result_text.delete(0.0,END)
submit_btn = Button(win, text=u'查询', command=submit)
submit_btn.place(x=205, y=80, width=35, height=25)
submit_btn2 = Button(win, text=u'清空', command=clean)
submit_btn2.place(x=250, y=80, width=35, height=25)

win.mainloop()


