import requests
url = 'https://www.kuaidi100.com/query'
dhl = input('输入快递公司(全拼)：')
id = input('输入%s的快递单号：'%dhl)

headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'csrftoken=UCcVb3x5dw_J_0VHW1w12g4EtU1zUEIqze-HMMGh9AE; WWWID=WWW977B61B5C1F47D0ADBDDEF01CBAF84C9; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1561365641,1561446113,1561446562,1561446610; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1561446610',
    'Host': 'www.kuaidi100.com',
    'Referer': 'https://www.kuaidi100.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
parameters = {
    'type': dhl,
    'postid': id,
    'temp': '0.47912186258122214',
    'phone': ''
}
res = requests.get(url,headers=headers,params=parameters)
json_express = res.json()
list_sign_for = json_express['data']
for sign_for in list_sign_for:
    time = sign_for['time']
    context = sign_for['context']
    print(time+' '+context)

