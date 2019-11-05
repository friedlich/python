# 如果一个请求的Content-Type设置为application/x-www-form-urlencoded，那么这个Post请求会被认为是Http Post表单请求，
# 那么请求主体将以一个标准的键值对和&的querystring形式出现。这种方式是HTML表单的默认设置，所以在过去这种方式更加常见。

# 其他形式的POST请求，是放到 Request payload 中（现在是为了方便阅读，使用了Json这样的数据格式），请求的Content-Type
# 设置为application/json;charset=UTF-8或者不指定。

## 使用requests模块post payload请求
import json
import requests
import datetime

postUrl = 'https://sellercentral.amazon.com/fba/profitabilitycalculator/getafnfee?profitcalcToken=en2kXFaY81m513NydhTZ9sdb6hoj3D'
# payloadData数据
payloadData = {
    'afnPriceStr': 10,
    'currency':'USD',
    'productInfoMapping': {
        'asin': 'B072JW3Z6L',
        'dimensionUnit': 'inches',
    }
}
# 请求头设置
payloadHeader = {
    'Host': 'sellercentral.amazon.com',
    'Content-Type': 'application/json',
}
# 下载超时
timeOut = 25
# 代理
proxy = "183.12.50.118:8080"
proxies = {
    "http": proxy,
    "https": proxy,
}
r = requests.post(postUrl, data=json.dumps(payloadData), headers=payloadHeader)
dumpJsonData = json.dumps(payloadData)
print(f"dumpJsonData = {dumpJsonData}")
res = requests.post(postUrl, data=dumpJsonData, headers=payloadHeader, timeout=timeOut, proxies=proxies, allow_redirects=True)
# 下面这种直接填充json参数的方式也OK
# res = requests.post(postUrl, json=payloadData, headers=header)
print(f"responseTime = {datetime.datetime.now()}, statusCode = {res.status_code}, res text = {res.text}")


# 这儿有个坏消息，那就是scrapy目前还不支持payload这种request请求。而且scrapy对formdata的请求也有很严格的要求
# 分析scrapy源码
# 文件：E:\Miniconda\Lib\site-packages\scrapy\http\request\form.py
class FormRequest(Request):

    def __init__(self, *args, **kwargs):
        formdata = kwargs.pop('formdata', None)
        if formdata and kwargs.get('method') is None:
            kwargs['method'] = 'POST'

        super(FormRequest, self).__init__(*args, **kwargs)

        if formdata:
            items = formdata.items() if isinstance(formdata, dict) else formdata
            # querystr = _urlencode(items, self.encoding)
            # 这儿写死了，当提交数据时，设置好Content-Type，也就是form data类型
            # 就算改写这儿，后面也没有对 json数据解析的处理
            if self.method == 'POST':
                self.headers.setdefault(b'Content-Type', b'application/x-www-form-urlencoded')
                # self._set_body(querystr)
            # else:
                # self._set_url(self.url + ('&' if '?' in self.url else '?') + querystr)
