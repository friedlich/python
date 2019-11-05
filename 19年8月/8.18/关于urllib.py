import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))
# print(response.status_code)