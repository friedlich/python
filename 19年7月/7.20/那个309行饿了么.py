import requests,json,base64,sys,csv
from PIL import Image

#【1】获取位置参数和选定地址
def get_position_info(ses):
    #准备url和params，发送请求
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

    #将搜索到的结果打印到屏幕
    print('以下，是与'+place+'相关的位置信息：\n')
    print('*'*75)   #分割线
    for n,v in enumerate(address_json):
        # print(str(n)+'. '+v['name']+'：'+v['short_address']+'\n')
        print('{}.【{}】: {}\n'.format(str(n),v['name'],v['short_address']))
    print('*'*75 + '\n\n')   #分割线

    #在结果中选择
    while True:
        address_num = int(input('请输入您选择位置的序号：'))
        if address_num in range(len(address_json)):
            break
        else:
            print('输入的序号有误,再试一次！')

    final_address = address_json[address_num]

    #根据选择结果，传出需要的返回值
    return final_address['geohash'],final_address['latitude'],final_address['longitude'],final_address['name']

#【2】搜索店铺
def find_shop(ses,params,pos):

    #尝试本地获取cookies，如果失败，就登录获取cookies，详见函数【2.1】【2.2】
    if open_get_cookies(ses) == False:

        login_get_cookies(ses)

    #准备url和params，发送请求

    restaurants_url = 'https://www.ele.me/restapi/shopping/restaurants'
    res = ses.get(restaurants_url,headers=headers,params=params)
    # print(res.text)
    print(params)

    if res.status_code == 401:
        print('本地cookies失效，尝试登录重新获取cookies')
        ses = login_get_cookies(ses)
        res = ses.get(restaurants_url,headers=headers,params=params)

    #将搜索到的店铺信息打印到屏幕
    print('-'*75)
    for n,i in enumerate(res.json()):
        # print(i)
        print('({})【{}】 距离{}{}米'.format(n+1,i['name'],pos,i['distance']))
        print('描述:{}'.format(i['description'].replace('\n','').replace(' ','')))
        print('链接:https://www.ele.me/shop/{}\n'.format(i['id']))
    print('-'*75)

#【2.1】读本地文件，获得cookies
def open_get_cookies(ses):
    #打开 cookies.txt，读取cookies
    try:
        with open(sys.path[0] + '\\cookies.txt','r') as f:
            cookies_str = f.read()
        #没抛异常说明有货，一系列操作，把cookies字符串变成cookies，赋值给session.cookies
        #返回True，告诉主程序，哥们我得手了，进行下一步吧
        cookies_dict = json.loads(cookies_str)
        cookies = requests.utils.cookiejar_from_dict(cookies_dict)
        ses.cookies = cookies
        print('载入本地cookies成功！\n')
        return True

        #抛异常,说明本地cookies文件不存在
        #返回False，让主程序还是登陆获取cookies吧
    except:
        print('载入本地cookies失败,尝试登录获取cookies！\n')
        return False

#【2.2】登录获得cookies
def login_get_cookies(ses):

    #死循环，如果登陆不成功就一直登，不达目的，誓不罢休
    while True:

        #初始登陆需要两个条件，一个是验证码，一个是token
        #调用send_code()函数，验证码会发送到手机上
        #token是发送验证码请求的回信，这里由send_code()函数的返回值给出
        #只要服务器发送验证码成功了，就会在XHR里的mobile_send_code的Preview里返回token
        #对于外地手机的话，服务器需要验证你才会发送验证码到你手机上，所以mobile_send_code的Preview里会返回message: 
        #"账户存在风险,需要滑动验证码"，滑动可怕呀
        token,tel = send_phone_code(ses)     #详见函数【2.2.1】

        #准备好url和data（data需要填入以上两个参数），发送请求，获取状态码
        #登陆成功后，cookies会自动写入session，我们只需要拿到状态码，判断登陆是否成功就可以了
        url_2 = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
        data_2 = {
                'mobile': tel,
                'scf': 'ms',
                'validate_code': input('请输入短信验证码：'),
                'validate_token': token
                }
        login_status = ses.post(url_2,headers=headers,data=data_2).status_code 

        if login_status == 200:

            #将cookies写入本地文本文件，以备下次使用，详见函数【2.2.2】
            save_cookies(ses.cookies) # 这里保存的显然只是你的登陆信息，cookies对应的session就是记录了用户登陆会话的信息
            ### 此时，你已经登陆完毕，你是在会话下进行一系列登陆操作的，(而session是会话过程中，服务器用来记录
            ### 特定用户会话的信息)所以服务器已经记录了你的会话信息，而session中存储了cookies的信息，服务器就可以根据
            ### 浏览器携带的cookies识别用户，可以在此时把session.cookies获取出来保存到本地，就相当于是当浏览器第一次
            ### 访问购物网页时，服务器会返回set cookies的字段给浏览器，而浏览器会把cookies保存到本地。所以下次只要在
            ### 发送请求时携带cookies，因为cookies里带有会话的编码信息，服务器立马就能辨认出这个用户，同时返回和这个
            ### 用户相关的特定编码的session

            print('恭喜登录成功!cookies已载入并存盘！\n')
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

        url_1 = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'

        # headers = {
        #           'origin':'https://h5.ele.me',
        #           'Referer':'https://h5.ele.me/login/',
        #           'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
        #           }

        data_1 = {
                'captcha_hash':captcha_hash,
                'captcha_value':captcha_value,
                'mobile': tel,
                'scf': "ms"
                }
        res = ses.post(url_1,headers=headers,data=data_1)

        code = res.status_code
        print(type(res))
        print(res.text)
        print('status code of login:' + str(code))

        #如果成功，拿到token
        if code == 200: #前三次登录没有图片验证过程
            token = res.json()['validate_token']
            print('验证码发送成功！状态码为{}，token为{}'.format(code,token))
            return token,tel

        #如果不成功，分情况讨论
        elif code == 400: #登录超过3次，网站会要求图片验证
            message = res.json()['message']
            print('验证码发送未成功！'+message)

            #如果需要图形验证码，发送图形码，兵分两路，拿到captcha_hash，填写图形码
            #也就是更新captcha_hash、captcha_value两个参数，再战
            if message in ['账户存在风险,需要图形验证码', '图形验证码错误']:
                captcha_hash = send_image_code(tel,ses)      #详见函数【2.2.1.1】
                captcha_value = input("请输入图片验证码：")

            #如果手机号被封，则更换手机号，清空另两个参数，再战
            elif message in ['错误的手机号码', '您的操作太快了，请明天再来吧']:
                tel = input('请换个手机号:')
                captcha_hash = ''
                captcha_value = ''

#【2.2.1.1】发送图片验证码，兵分两路，返回captcha_hash，保存图片到本地
def send_image_code(tel,ses):

    url_3 = ' https://h5.ele.me/restapi/eus/v3/captchas'
    data_3 = {'captcha_str': tel}
    # 提取验证码。
    cap = ses.post(url_3, headers=headers, data=data_3).json()
    # print(cap)

    captcha_image = cap['captcha_image']
    captcha_hash = cap['captcha_hash']

    bs64 = captcha_image.split(',')[-1]
    # 验证码字符串转图形文件保存到本地
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
        #把cookies对象转化成字典，再转化为字符串，写入文本文件
        cookies_dict = requests.utils.dict_from_cookiejar(cookies)
        cookies_str = json.dumps(cookies_dict)
        f.write(cookies_str)

if __name__ == '__main__':

    #创建session对象，该对象将一直在本程序中重复使用
    session = requests.session()

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    #调用get_position_info函数，获取位置信息，详见函数【1】
    geohash,latitude,longitude,pos = get_position_info(session)

    limit = 10 #每页显示数量

    page = 0   #起始页

    #设置初始参数
    params={
    'extras[]': 'activities',
    'geohash': geohash,
    'latitude': latitude,
    'limit': limit,
    'longitude': longitude,
    'offset': page*limit, # 无效的offset
    'terminal': 'web'
    }

    #初始显示店铺，详见函数【2】
    find_shop(session,params,pos)

    #修改参数
    while True:

        #接收用户输入
        input_info = input('显示更多输入a，退出输入q：')
        if input_info =='a':
            # page += 1
            limit += 10
            # while True:
            #     limit = 30 # limit限制数量为30
            #     break
        elif input_info == 'q':
            print('欢迎下次光临饿了吗！')
            break
        else:
            print('你的输入有误，请重新输入！')

        # print(limit)
        # print(page*limit)
        #修改参数   
        ### 其实吧，改了也没用，因为等下你会载入本地的cookies，它记录的永远是你之前浏览的第一页24家餐馆的信息，就很奇怪，
        ### cookies记录的就是你等下看到的，改params的本质应该是想改cookies，但是你的cookies是本地载入的，是改不了的，
        ### 所以，无论你怎么输入'a'，终端只会展示cookies记录的你第一次浏览的餐馆信息，但是我可以尝试修改一下代码

        ### 讲道理，这个理解可能不对，因为你重新换地址的话也是直接载入本地cookies的，但是这时终端显示的餐馆内容会变化的，
        ### 这说明并不是本地cookies的问题，不然的话如果offset不能在函数【2】中修改的话，geohash,latitude,longitude也
        ### 是改不了的,很明显，这些在重新运行py文件换地址的时候都修改了。所以，我觉得根源应该是find_shop函数中传入的这个
        ### session搞的鬼，因为显示更多的时候说实话用的还是之前的session,session保存了会话信息，保存了页面信息，重新换
        ### 地址的时候是重新创建session,这是两者的区别，也应该是问题所在。换地址的时候是重新创建回话，然后调用get_position
        ### _info函数获取了geohash,latitude,longitude，设置了初始参数，然后再调用find_shop(session,params,pos)，传入
        ### session,然后res = ses.get(restaurants_url,headers=headers,params=params)这一步，三个点都有。回到之前输入
        ### a显示更多，用的还是之前的session,所以重新创建？还是不对啊我去了！！！为什么呢

        ### 可能问题的答案是我的代码根本没有问题，问题在于这个offset失效了，只有limit在起作用，我试了很多次，说实话这个
        ### offset从未产生过作用，limit到是一直在起作用，'limit': 10，'limit': '20'都起了作用；'offset': 10，'offset': 
        ### '5'都不起作用，讲真的，这个饿了么网站是真的坑
        
        ### 那么我现在来总结一下吧，cookies存储的是你的登陆信息，cookies里面携带了session的编码信息，服务器可以根据浏览器
        ### 携带的cookies识别用户，同时返回和这个用户相关的特定编码的session(session是会话过程中，服务器用来记录特定用户
        ### 会话的信息)。这个时候，用户就可以在会话下去发送各种请求，这个会话的话浏览器应该是有记录的。所以只要在发送请求时
        ### 带着cookies，对于session来说(session中又存储了cookies的信息)，只需要把本地存储的cookies赋值给session.cookies
        ### ，就可以直接在会话下发送获取餐馆信息的请求，免去之前登陆的请求。说实话，为什么要登陆呢，其实就是为了获取cookies，
        ### 你在一些需要登陆的网站发送各种请求时，都需要携带cookies，这些网站服务器必须要认识你你才会对你的请求作出有效响应

        params = {
        'extras[]': 'activities',
        'geohash': geohash,
        'latitude': latitude,
        'limit':str(limit), 
        'longitude': longitude,
        'offset': '5', # 无效的offset
        # 'offset': str(page*limit), 
        'terminal': 'web'
        }
        #重新显示，详见函数【2】
        # session = requests.session()
        find_shop(session,params,pos)
