import requests,json,base64,sys,csv
from PIL import Image

#【1】获取位置参数和选定地址
def get_position_info(ses):

    address_url = 'https://www.ele.me/restapi/bgs/poi/search_poi_nearby'
    place = input('请输入你的收货地址：')
    params = {
        'geohash': 'wtw3sjq6n6um',
        'keyword': place,
        'latitude': '31.23037', 
        'limit': '20', 
        'longitude': '121.473701', 
        'type': 'nearby'
        }
    address_json =json.loads(ses.get(address_url,headers=headers,params=params).text)

    print('以下，是与'+place+'相关的位置信息：\n')
    print('*'*75)   #分割线
    for n,v in enumerate(address_json):
        print('{}.【{}】: {}\n'.format(str(n),v['name'],v['short_address']))
    print('*'*75 + '\n\n')   #分割线

    while True:
        address_num = int(input('请输入您选择位置的序号：'))
        if address_num in range(len(address_json)):
            break
        else:
            print('输入的序号有误,再试一次！')

    final_address = address_json[address_num]

    return final_address['geohash'],final_address['latitude'],final_address['longitude'],final_address['name']

#【2】搜索店铺
def find_shop(ses,params,pos):

    if open_get_cookies(ses) == False:   
        login_get_cookies(ses)

    restaurants_url = 'https://www.ele.me/restapi/shopping/restaurants'
    res = ses.get(restaurants_url,headers=headers,params=params)
    if res.status_code == 401:
        print('本地cookies失效，尝试登录重新获取cookies')
        ses = login_get_cookies(ses)
        res = ses.get(restaurants_url,headers=headers,params=params)

    print('-'*75)
    for n,i in enumerate(res.json()):
        print('({})【{}】 距离{}{}米'.format(str(n+1),i['name'],pos,i['distance'])) #TypeError: string indices must be integers
        print('描述:{}'.format(i['description'].replace('\n','').replace(' ','')))
        print('链接:https://www.ele.me/shop/{}\n'.format(i['id']))
    print('-'*75)

#【2.1】读本地文件，获得cookies
def open_get_cookies(ses):

    try:
        with open(sys.path[0] + '\\cookies.txt','r') as f:
            cookies_str = f.read()
        cookies_dict = json.loads(cookies_str)
        cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        ses.cookies = cookies
        print('载入本地cookies成功！\n')
        return True
    except:
        print('载入本地cookies失败,尝试登录获取cookies！\n')
        return False

#【2.2】登录获得cookies
def login_get_cookies(ses):

    while True:

        token,tel = send_phone_code(ses)

        url_2 = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
        data_2 = {
                'mobile': tel,
                'scf': 'ms',
                'validate_code': input('请输入短信验证码：'),
                'validate_token': token
                }
        login_status = ses.post(url_2,headers=headers,data=data_2).status_code

        if login_status == 200:
            save_cookies(ses.cookies)
            print('恭喜登录成功!cookies已载入并存盘！\n')
            break
    return ses
     
#【2.2.1】发送验证码，兵分两路，手机拿验证码，回信拿token
def send_phone_code(ses):

    tel = input('请输入电话号码：')
    captcha_hash = ''
    captcha_value = ''

    while True:
        url_1 = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
        data_1 = {
                'captcha_hash':captcha_hash,
                'captcha_value':captcha_value,
                'mobile': tel,
                'scf': "ms"
                }
        res = ses.post(url_1,headers=headers,data=data_1)
        code = res.status_code

        if code == 200:
            token = res.json()['validate_token']
            print('验证码发送成功！状态码为{}，token为{}'.format(code,token))
            return token,tel
        elif code == 400:
            message = res.json()['message']
            print('验证码发送未成功！'+message)
            if message in ['账户存在风险,需要图形验证码', '图形验证码错误']:
                captcha_hash = send_image_code(tel,ses)   
                captcha_value = input("请输入图片验证码：")
            elif message in ['错误的手机号码', '您的操作太快了，请明天再来吧']:
                tel = input('请换个手机号:')
                captcha_hash = ''
                captcha_value = ''

#【2.2.1.1】发送图片验证码，兵分两路，返回captcha_hash，保存图片到本地
def send_image_code(tel,ses):

    url_3 = ' https://h5.ele.me/restapi/eus/v3/captchas'
    data_3 = {'captcha_str': tel}
    cap = ses.post(url_3, headers=headers, data=data_3).json()

    captcha_image = cap['captcha_image']
    captcha_hash = cap['captcha_hash']

    bs64 = captcha_image.split(',')[-1]
    imagedata = base64.b64decode(bs64)

    file = open(sys.path[0]+'\\captcha.jpg', "wb")
    file.write(imagedata)
    file.close()

    im = Image.open(sys.path[0]+'\\captcha.jpg')
    im.show()#展示验证码图形

    return captcha_hash

#【2.2.2】cookies存盘
def save_cookies(cookies):

    with open(sys.path[0] + '\\cookies.txt','w+',encoding = 'utf-8') as f:
        cookies_dict = requests.utils.dict_from_cookiejar(cookies)
        cookies_str = json.dumps(cookies_dict)
        f.write(cookies_str)

if __name__ == '__main__':

    session = requests.session()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
    
    geohash,latitude,longitude,pos = get_position_info(session)
    limit = 10

    params={
    'extras[]': 'activities',
    'geohash': geohash,
    'latitude': latitude,
    'limit': limit,
    'longitude': longitude,
    'offset': 0, # 无效的offset
    'terminal': 'web'
    }
    find_shop(session,params,pos)

    while True:

        input_info = input('显示更多输入a，退出输入q：')
        if input_info =='a':
            limit += 10
        elif input_info == 'q':
            print('欢迎下次光临饿了吗！')
            break
        else:
            print('你的输入有误，请重新输入！')
        params = {
            'extras[]': 'activities',
            'geohash': geohash,
            'latitude': latitude,
            'limit': limit, 
            'longitude': longitude,
            'offset': 0, # 无效的offset
            'terminal': 'web'
            }
        find_shop(session,params,pos)