import requests,openpyxl
from bs4 import BeautifulSoup
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='表'
sheet['A1']='房屋名称'
sheet['B1']='楼层信息'
sheet['C1']='类型'
sheet['D1']='地址及交通信息'
sheet['E1']='价格'
sheet['F1']='面积'
sheet['G1']='页面链接'

for x in range(5):
    url='http://www.ziroom.com/z/nl/z2-s4%E5%8F%B7%E7%BA%BF.html'
    # print(url)
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',}
    res=requests.get(url,headers=headers)
    bs=BeautifulSoup(res.text,'html.parser')
    li_list=bs.find_all('li',class_='clearfix')
    for li in li_list:
        txt = li.find('div',class_ = 'txt')
        info = txt.h3.a.text
        href = txt.h3.a['href']
        area,floor,type = txt.find('div',class_ = 'detail').find_all('p')[0].text.replace('\n','').replace(' ','').split('|')
        # 解包，就是直接对列表，元组等取值 a,b,c = [1,2,3]
        # print(info,floor,position,'',area,href)
        position = txt.find('div',class_ = 'detail').find_all('p')[1].text
        num = li.find(class_="price").find_all(class_="num")
        price = 0
        for i in num:
            price_num = i.content
            price += price_num
        sheet.append([info,floor,type,position,price,area,href])
        
wb.save(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.09\ziru2.xlsx')