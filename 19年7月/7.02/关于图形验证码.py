import requests,json
import base64,sys
from PIL import Image
session = requests.Session()
headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
			 } # 'User-Agent': '此处输入自己的浏览器的User-Agent信息'
url = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
# 登录的网址。
tel = input('请输入手机号：')
data = {'captcha_hash': '',
        'captcha_value': '',
        'mobile': tel,
        'scf': 'ms'
        }
# 登录的参数。
login = session.post(url, headers=headers, data=data)
code = login.status_code
print(type(login))
print('status code of login: ' + str(code))
if code == 200:#前三次登录没有图片验证过程
    token = login.json()['validate_token']
    print('成功发送,返回无图片验证码')
    url = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
    code = input('请输入手机验证码：')
    data2 = {
        'mobile': tel,
        'scf': 'ms',
        'validate_code': code,
        'validate_token': token
    }
    verify = session.post(url, headers=headers, data=data2)
    print('status_code:'+str(verify.status_code))#打印返回值
elif code == 400:#登录超过3次，网站会要求图片验证
    print('有图片验证码')
    while True:
        key = True
        while key:
            url = ' https://h5.ele.me/restapi/eus/v3/captchas'
            data2 = {'captcha_str': tel}
            # 提取验证码。
            cap = session.post(url, headers=headers, data=data2)
            code = cap.status_code
            print(cap.json())
            strCap = cap.json()['captcha_image'].replace('data:image/jpeg;base64,', '')
            hash1 = cap.json()['captcha_hash']
            # 验证码字符串转图形文件保存到本地
            x = base64.b64decode(strCap)
            file = open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.02\captcha.jpg', "wb")
            file.write(x)
            file.close()
            im = Image.open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.02\captcha.jpg')
            im.show()#展示验证码图形
            captcha_value = input('输入验证码:')
            #将图片验证码作为参数post到饿了吗服务器登录
            url = ' https://h5.ele.me/restapi/eus/login/mobile_send_code'
            data = {'captcha_hash': hash1,
                'captcha_value': captcha_value,
                'mobile': tel,
                'scf': 'ms'
                }
        # 将验证码发送到服务器。
            login = session.post(url, headers=headers, data=data)
            print(login.json())
            # 加判断条件
            if 'validate_token' in login.json():
                key = False
            else:
                continue
        token = login.json()['validate_token']
        url = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
        code = input('请输入手机验证码：')
        data2 = {
            'mobile': tel,
            'scf': 'ms',
            'validate_code': code,
            'validate_token': token
        }
        verify = session.post(url, headers=headers, data=data2)#验证手机验证码
        print('status_code:'+str(verify.status_code))#打印返回值
        if verify.status_code == 200:
            break
        else:
            continue

