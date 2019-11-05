import requests
from requests.exceptions import ConnectTimeout
try:
    response = requests.get('http://httpbin.org/get', timeout=0.1)
    print(response.status_code)
except ConnectTimeout:
    print('ConnectTimeout')