import requests
import sys

response = requests.get('https://github.com/favicon.ico')
print(type(response.text),type(response.content))
with open(sys.path[0] + '\\' + 'favicon.ico','wb') as f:
    f.write(response.content)
    f.close()