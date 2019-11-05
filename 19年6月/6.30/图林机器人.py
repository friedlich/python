import requests,json

session = requests.session()
url = r'http://openapi.tuling123.com/openapi/api/v2'
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
while True:
    sendmessage = input('快与小灵互动吧:')
    data = {
 "reqType":0,
    "perception": {
        "inputText": {
            "text": sendmessage
        },    
    },
    "userInfo": {
        "apiKey": 'ebb6ffd7edec4f3aab8f6c7fe2cf00c7',
        "userId": 'demo'
    }
        }
    if sendmessage == '':
        break
    res = session.post(url,data=json.dumps(data),headers=headers)
    results = res.json()['results']
    for result in results:
        print('小灵回复:',result['values']['text'],'\n')