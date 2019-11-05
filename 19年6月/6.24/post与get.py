import requests

url_1 = 'https://…'
headers = {'user-agent':''}
data = {}
# 定义url，headers和data

login_in = requests.post(url_1,headers=headers,data=data)
cookies = login_in.cookies
# 完成登录，获取cookies

url_2 = 'https://…'
params = {}
# 定义url和params

response = requests.get(url_2,headers=headers,params=params,cookies=cookies)
# 带着cookies重新发起请求