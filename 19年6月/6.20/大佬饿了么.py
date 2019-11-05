import requests
import base64
import time
import json


headtxt='''
**********************************************
名称：今天你饿了吗
作者：kython，ky是开心的ky，thon是python的thon
鸣谢：部分代码参考起航大佬，特表感谢
**********************************************
'''
#【0】主函数
def main():
    #输出片头
    print(headtxt)
    input('按任意键继续...')
    print()

    #创建session对象，该对象将一直在本程序中重复使用
    session = requests.session()

    #调用get_position_info函数，获取位置信息，详见函数【1】
    geohash,latitude,longitude,pos = get_position_info(session)

    limit = 5  #每页显示数量

    page = 1   #起始页

    #设置初始参数
    params = {
    'extras[]': 'activities',
    'geohash': geohash,
    'latitude': latitude,
    'limit':limit, 
    'longitude': longitude,
    'offset': page*limit, 
    'terminal': 'web'
    }

    #初始显示店铺，详见函数【2】
    find_shop(session,params,pos)

    #修改参数
    while True:
        
        #接收用户输入
        input_info = input('显示更多输入a，退出输入q：')
        if input_info =='a':
            while True:
                limit = 30
                break
        elif input_info == 'q':
            print('欢迎下次光临饿了吗！')
            break
        else:
            print('你的输入有误，请重新输入！')

        #修改参数
        params = {
        'extras[]': 'activities',
        'geohash': geohash,
        'latitude': latitude,
        'limit':str(limit), 
        'longitude': longitude,
        'offset': str(page*limit), 
        'terminal': 'web'
        }
        #重新显示，详见函数【2】
        find_shop(session,params,pos)
        
#【1】获取位置参数和选定地址
def get_position_info(ses):
    #准备url和params，发送请求
    url = 'https://www.ele.me/restapi/v2/pois'
    params = {
        'extras[]': 'count',
        'geohash': 'wxrvbf2xqqkb',
        'keyword': input('请输入你的收货地址:'),
        'limit': '20',
        'type': 'nearby',
        }    
    pjson =ses.get(url,params=params).json()

    #将搜索到的结果打印到屏幕
    print('*'*75)   #分割线
    for n,v in enumerate(pjson):
        print(n,'【{}】'.format(v['name']),v['address'])
    print('*'*75)   #分割线
    
    #在结果中选择
    while True:
        i = int(input('请在以上列表中选择具体地点，并输入序号：'))
        if i in range(len(pjson)):
            break
        else:
            print('输入的序号有误,再试一次！')

    pdic = pjson[i]

    #根据选择结果，传出需要的返回值

    return pdic['geohash'],pdic['latitude'],pdic['longitude'],pdic['name']
    
#【2】搜索店铺
def find_shop(ses,params,pos):


    
    #尝试本地获取cookies，如果失败，就登录获取cookies，详见函数【2.1】【2.2】
    if open_get_cookies(ses) == False:
        
        login_get_cookies(ses)
        
    #准备url和params，发送请求
    
    url = 'https://www.ele.me/restapi/shopping/restaurants'
    res = ses.get(url,params=params)

    if res.status_code == 401:
        print('本地cookies失效，尝试登录重新获取cookies')
        ses = login_get_cookies(ses)
        res = ses.get(url, params=params)
        
    #将搜索到的店铺信息打印到屏幕
    print('-'*75)
    for n,i in enumerate(res.json()):
        print(i)
        print('({})【{}】 距离{}{}米'.format(n+1,i['name'],pos,i['distance']))
        print('地址:{}'.format(i['address']))
        print('链接:https://www.ele.me/shop/{}'.format(i['id']))
    print('-'*75)



#【2.1】读本地文件，获得cookie
def open_get_cookies(ses):
    #打开 cookies_txt，读取cookies
    try:
        with open('cookies.txt','r') as cookies_txt:
            cookies_str = cookies_txt.read()

        #没抛异常说明有货，一些列操作，把cookies字符串变成cookies，赋值给session.cookies
        #返回True，告诉主程序，哥们我得手了，进行下一步吧
        cookies_dict = json.loads(cookies_str)
        cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        ses.cookies = cookies
        print('载入本地cookies成功！')
        return True
        
        #抛异常,说明本地cookies文件不存在
        #返回False，让主程序还是登陆获取cookies吧
    except:
        print('载入本地cookies失败,尝试登录获取cookies！')
        return False
          

#【2.2】登录获得cookies
def login_get_cookies(ses):
    
    #死循环，如果登陆不成功就一直登，不达目的，誓不罢休
    while True:
        
        #初始登陆需要两个条件，一个是验证码，一个是token
        #调用send_code()函数，验证码会发送到手机上
        #token是发送验证码请求的回信，这里由send_code()函数的返回值给出
        token,tel = send_phone_code(ses)     #详见函数【2.2.1】

        #准备好url和data（data需要填入以上两个参数），发送请求，获取状态码
        #登陆成功后，cookies会自动写入sesssion，我们只需要拿到状态码，判断登陆是否成功就可以了
        url = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
        data = {
            "mobile": tel,
            "validate_code": input('请输入短信验证码:'),
            "validate_token": token,
            "scf": "ms"
            }
        login_status = ses.post(url, data=data).status_code  

        if login_status == 200:
            
            #将cookies写入本地文本文件，以备下次使用，详见函数【2.2.2】
            save_cookies(ses.cookies)
            
            print('恭喜登录成功!cookies已载入并存盘！')
            break
    return ses

        
#【2.2.1】发送验证码，兵分两路，手机拿验证码，回信拿token
def send_phone_code(ses):

    #在循环外设置初始值，tel在电话号被封时修改，其他两个在需要图片验证码时修改
    
    tel = input('请输入电话号码：')
    captcha_hash = ''
    captcha_value = ''
    
    while True:

        #函数click_send_code()需要三个参数，tel、captcha_hash、captcha_value，返回值为token
        #tel参数用于接收登录验证码，如果手机号被封，则需要更换，循环外为初始值
        #captcha_hash、captcha_value在有图片验证码时使用，没有图片验证码时为空
        #captcha_value是图片验证码的值，captcha_hash为图片验证码返回的秘钥，相当于之前的token
        #发现验证码都是兵分两路，一路是手机或者图片显示验证码，一路是自己藏着一个秘钥


        url = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'

        headers = {'origin':'https://h5.ele.me',
                   'Referer':'https://h5.ele.me/login/',
                   'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
                   }

        data = {'captcha_hash':captcha_hash,
                'captcha_value':captcha_value,
                'mobile': tel,
                'scf': "ms"
                }

        res = ses.post(url,headers = headers,data = data)
        
        code = res.status_code
        
        #如果成功，拿到token
        if code == 200:
            token = res.json()['validate_token']
            print('验证码发送成功！状态码为{}，token为{}'.format(code,token))
            return token,tel
        
        #如果不成功，分情况讨论   
        elif code == 400:
            message = res.json()['message']
            print('验证码发送未成功！'+message)


            #如果需要图形验证码，发送图形码，兵分两路，拿到captcha_hash，填写图形码
            #也就是更新captcha_hash、captcha_value两个参数，再战
            if message in ['账户存在风险,需要图形验证码', '图形验证码错误']:
               captcha_hash = send_image_code(tel,ses)            #详见函数【2.2.1.1】 
               captcha_value = input("请输入图片验证码：")

            #如果手机号被封，则更换手机号，清空另两个参数，再战
            elif message in ['错误的手机号码', '您的操作太快了，请明天再来吧']:
                tel = input('请换个手机号:')
                captcha_hash = ''
                captcha_value = ''
                
#【2.2.1.1】发送图片验证码，兵分两路，返回captcha_hash，保存图片到本地
                
def send_image_code(tel,ses):
    
    url1 = 'https://h5.ele.me/restapi/eus/v3/captchas'
    data1 = {"captcha_str": tel}
    res = ses.post(url1,data = data1).json()

    captcha_image = res['captcha_image']   
    captcha_hash = res['captcha_hash']
    
    bs64 = captcha_image.split(',')[-1]
    imagedata = base64.b64decode(bs64)
    
    file = open('1.jpg',"wb")
    file.write(imagedata)
    file.close()
    
    return captcha_hash
        
                   
        
#【2.2.2】cookies存盘
def save_cookies(cookies):
    with open('cookies.txt','w+',encoding = 'utf-8') as cookies_txt:
        #把cookies对象转化成字典，再转化为字符串，写入文本文件
        cookies_dict = requests.utils.dict_from_cookiejar(cookies)
        cookies_str = json.dumps(cookies_dict)
        cookies_txt.write(cookies_str)

        
#调用主函数
main()

# 我觉得可与研究一下大佬的代码，优化再优化
