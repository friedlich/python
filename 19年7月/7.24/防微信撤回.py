import requests,json
import itchat 

userId = '77'
apiKey = 'cc808f580b7a4b7caaa9f1f31e6d602e'

def get_response(msg):
    api = 'http://openapi.tuling123.com/openapi/api/v2'
    data = {
        'key':apiKey,
        'info':msg,
        'userid':userId 
    }
    try:
        res = requests.post(api,json.dumps(data))
        return json.loads(res).get('text')
    except:
        return

@itchat.msg_register(['Text','Map','Card','Note','Sharing','Picture'])

def tuling_reply(msg):
    defaulteplay = '有事留言'
    reply = get_response(msg['Text'])
    return reply or defaulteplay

itchat.auto_login(hotReload=True)
itchat.run()



