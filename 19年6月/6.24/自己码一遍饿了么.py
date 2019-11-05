import requests,base64
from PIL import Image

address_url = 'https://www.ele.me/restapi/bgs/poi/search_poi_nearby?'
place = input('请输入你的收货地址：')
params = {
    'geohash': 'wtw3sjq6n6um',
    'keyword': place,
    'latitude': '31.23037',
    'limit': '20',
    'longitude': '121.473701',
    'type': 'nearby'
    }
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
address_res = requests.get(address_url,headers=headers,params=params)
address_json = address_res.json()

print('以下，是与'+place+'相关的位置信息：\n')
n=0
for address in address_json:
    print(str(n)+'. '+address['name']+'：'+address['short_address']+'\n')
    n = n+1
address_num = int(input('请输入您选择位置的序号：'))
final_address = address_json[address_num]


session = requests.session()
url_1 = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
tel = input('请输入手机号：')
data_1 = {
    'captcha_hash':'',
    'captcha_value':'',
    'mobile': tel,
    'scf': "ms"
}
login = session.post(url_1,headers=headers,data=data_1)
code = login.status_code
print(type(login))
print(login.text)
print('status code of login:' + str(code))
if code == 200: #前三次登录没有图片验证过程
    token = login.json()['validate_token']
    url_2 = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
    code = input('请输入手机验证码：')
    data_2 = {
        'mobile': tel,
        'scf': 'ms',
        'validate_code': code,
        'validate_token': token
    }
    session.post(url_2,headers=headers,data=data_2)
elif code == 400: #登录超过3次，网站会要求图片验证
    print('有图形验证码')
    url_3 = 'https://h5.ele.me/restapi/eus/v3/captchas'
    data_3 = {'captcha_str': "19921876546"}
    # 提取验证码。
    cap =session.post(url_3,headers=headers,data=data_3)
    hash = cap.json()['captcha_hash']
    value = cap.json()['captcha_image'].replace('data:image/jpeg;base64,','')
    # 验证码字符串转图形文件保存到本地
    x = base64.b64decode(value)
    file = open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\7.02\captcha.jpg','wb')
    file.write(x)
    file.close()
    im = Image.open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\7.02\captcha.jpg')
    im.show() #展示验证码图形
    captche_value = input('请输入验证码：')
    #将图片验证码作为参数post到饿了吗服务器登录
    url_1 = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
    data_4 = {
    'captcha_hash': hash,
    'captcha_value': captche_value,
    'mobile': tel,
    'scf': "ms"
    }
    # 将验证码发送到服务器。
    login = session.post(url_1,headers=headers,data=data_4)
    print(login.json())
    token = login.json()['validate_token']
    url_2 = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
    code = input('请输入手机验证码：')
    data_2 = {
        'mobile': tel,
        'scf': 'ms',
        'validate_code': code,
        'validate_token': token
    }
    session.post(url_2,headers=headers,data=data_2)

restaurants_url = 'https://www.ele.me/restapi/shopping/restaurants'
params={
    'extras[]': 'activities',
    'geohash': final_address['geohash'],
    'latitude': final_address['latitude'],
    'limit': '24',
    'longitude': final_address['longitude'],
    'offset': '0',
    'terminal': 'web'
}
restaurants_res = session.get(restaurants_url,headers=headers,params=params)
restaurants_json = restaurants_res.json()
for restaurant in restaurants_json:
    print(restaurant['name'])
