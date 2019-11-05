import requests,json
#调用了两个模块。requests负责上传和下载数据，json负责解析。

word = input('你想翻译什么呀？')
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
#使用post需要一个链接。
data={'i': word,
      'from': 'AUTO',
      'to': 'AUTO',
      'smartresult': 'dict',
      'client': 'fanyideskweb',
      'doctype': 'json',
      'version': '2.1',
      'keyfrom': 'fanyi.web',
      'action': 'FY_BY_REALTIME',
      'typoResult': 'false'}
#将需要post的内容，以字典的形式记录在data内。
r = requests.post(url,data)
#post需要输入两个参数，一个是刚才的链接，一个是data，返回的是一个Response对象。
answer=json.loads(r.text)
#你可以自己尝试print一下r.text的内容，然后再阅读下面的代码。
# print(r.text)
print ('翻译的结果是：'+answer['translateResult'][0][0]['tgt'])