import requests,json

userId = '64'
apiKey = 'ebb6ffd7edec4f3aab8f6c7fe2cf00c7'

def robot(content):
    api = 'http://openapi.tuling123.com/openapi/api/v2'
    data = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": content
            },
        },
        "userInfo": {
            "apiKey": apiKey,
            "userId": userId
        }
    }
    json_data = json.dumps(data)
    res = requests.post(api,data=json_data)
    robot_res = json.loads(res.text)
    print(robot_res['results'][0]['values']['text'])

for i in range(3):
    content = input('talk:')
    robot(content)
    if i == 2:
        break




