import requests
import json

response = requests.get('http://httpbin.org/get')
print(type(response.text))
print(response.json())
print(type(response.json()))
print(json.loads(response.text))
print(type(json.loads(response.text)))
