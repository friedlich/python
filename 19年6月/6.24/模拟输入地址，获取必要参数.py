# 本步骤不需要模拟登录
# 在模拟该请求时需要用到城市的geohash值，可在XHR里查看自己城市的geohash值

import requests
# 导入requests模块。
address_url = 'https://www.ele.me/restapi/v2/pois?'
# 你能够在【Headers】-【General】里找到这个链接。
place = input('请输入你的收货地址：')
# 使用input输入收获地址，赋值给place。
# 因为我们的geohash使用了深圳的值，所以推荐你测试的时候使用“腾讯大厦”。
params = {'extras[]':'count','geohash':'ws105rz9smwm','keyword':place,'limit':'20','type':'nearby'}
# 将要传递的参数封装成字典，键与值都要用字符串，其中keyword对于的值是place。
address_res = requests.get(address_url,params=params)
# 发起请求，将响应的结果，赋值给address_res
address_json = address_res.json()
# 将响应的结果转为列表/字典。

print('以下，是与'+place+'相关的位置信息：\n')
n=0
# 添加一个计数器，作为序号。
for address in address_json:
# 遍历我们刚爬取的地址列表。
    print(str(n)+'. '+address['name']+'：'+address['short_address']+'\n')
    # 打印序号，地址名，短地址。
    n = n+1
    # 给计数器加1。
address_num = int(input('请输入您选择位置的序号：'))
# 让用户选择序号。
final_address = address_json[address_num]
# 确认地址。

print(final_address['geohash'])
print(final_address['latitude'])
print(final_address['longitude'])