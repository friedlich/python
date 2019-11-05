import urllib.request

proxy_handler = urllib.request.ProxyHandler({'http':'http://127.0.0.1:9743',
'https':'https://127.0.0.1:9743'})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://httpbin.org/get')
print(response.read())