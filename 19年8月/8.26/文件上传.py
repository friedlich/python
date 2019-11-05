import requests
import sys

files = {'file': open(sys.path[0] + '\\' + 'favicon.ico', 'rb')}
response = requests.post('http://httpbin.org/post', files=files)
print(response.text)
