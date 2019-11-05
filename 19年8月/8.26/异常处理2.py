import requests
from requests.exceptions import ReadTimeout, ConnectTimeout, RequestException
try:
    response = requests.get('http://httpbin.org/get',timeout = 0.1)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except ConnectTimeout:
    print('Connection error')
except RequestException:
    print('Error')

