import requests,base64,sys,csv
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
    # print(str(n)+'. '+address['name']+'：'+address['short_address']+'\n')
    print('{}.【{}】: {}\n'.format(str(n),address['name'],address['short_address']))
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
} ### 遇到ｒｅｑｕｅｓｔ　ｐａｙｌｏａｄ时，要用ｊｓｏｎ．ｄｕｍｐｓ（）把数据封装一下再添加进请求
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
    while True:
        key = True
        while key:
            url_3 = ' https://h5.ele.me/restapi/eus/v3/captchas'
            data_3 = {'captcha_str': tel}
            # 提取验证码。
            cap = session.post(url_3, headers=headers, data=data_3)
            code = cap.status_code
            print(cap.json())
            strCap = cap.json()['captcha_image'].replace('data:image/jpeg;base64,', '')
            hash1 = cap.json()['captcha_hash']
            # 验证码字符串转图形文件保存到本地
            x = base64.b64decode(strCap)
            file = open(sys.path[0]+'\\captcha.jpg', "wb")
            file.write(x)
            file.close()
            im = Image.open(sys.path[0]+'\\captcha.jpg')
            im.show()#展示验证码图形
            captcha_value = input('输入验证码:')
            #将图片验证码作为参数post到饿了吗服务器登录
            url_1 = ' https://h5.ele.me/restapi/eus/login/mobile_send_code'
            data_4 = {'captcha_hash': hash1,
                'captcha_value': captcha_value,
                'mobile': tel,
                'scf': 'ms'
                }
        # 将验证码发送到服务器。
            login = session.post(url_1, headers=headers, data=data_4)
            print(login.json())
            # 加判断条件
            if 'validate_token' in login.json():
                key = False
            else:
                continue
        token = login.json()['validate_token']
        url_2 = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
        code = input('请输入手机验证码：')
        data_2 = {
            'mobile': tel,
            'scf': 'ms',
            'validate_code': code,
            'validate_token': token
        }
        verify = session.post(url_2, headers=headers, data=data_2)#验证手机验证码
        print('status_code:'+str(verify.status_code))#打印返回值
        if verify.status_code == 200:
            break
        else:
            continue

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

with open(sys.path[0]+'\\restaurants.csv','w',newline='',encoding='utf_8_sig') as f:
    writer = csv.writer(f)
    for restaurant in restaurants_json:
        writer.writerow([restaurant['name']]) 
        # 记住了，writerow()里面一定要用[]号，这样才一次性写入，不然的话写入的东西全用,号分开，看着贼难受
        # writer.writerow(['今天','明天','后天'])鉴于此，不加[]不成列表的话它直接把你的字符串当成迭代对象分割: 
        # '汉堡王'>>>汉,堡,王

# 这还远远没有结束