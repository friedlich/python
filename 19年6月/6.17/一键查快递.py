import requests
#调用requests模块，负责上传和下载数据

logisticsName = input('你的快递是什么物流呀？')
courierNum = input('你的快递单号是什么呀？')

url = 'https://www.kuaidi100.com/query'
#使用get需要一个链接

headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

params = {
          'type': logisticsName,
          'postid': courierNum,
          'temp': '0.9661515218223198',
          'phone':''
          }
#将需要get的内容，以字典的形式记录在params内

r = requests.get(url, params=params,headers=headers)
#get需要输入两个参数，一个是刚才的链接，一个是params，返回的是一个Response对象
result = r.json()

print ('最新物流状态：'+ result['data'][0]['context'])
#记得观察preview里面的参数哦


# 就没有一个可以查到的快递么，我真得是服了
