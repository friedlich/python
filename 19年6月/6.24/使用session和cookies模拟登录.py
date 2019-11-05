import requests
session = requests.session()
# 创建会话
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
# 添加请求头，避免被反爬虫
url_1 = 'https://h5.ele.me/restapi/eus/login/mobile_send_code'
# 发送验证码的网址
tel = input('请输入手机号码：')
data_1 = {'captcha_hash':'',
        'captcha_value':'',
        'mobile':tel,
        'scf':''}
# 发送验证码的参数
token = session.post(url_1, headers=headers, data=data_1).json()['validate_token']
# 在会话下，模拟获取验证码的请求

url_2 = 'https://h5.ele.me/restapi/eus/login/login_by_mobile'
code = input('请输入手机验证码：')
data_2 = {'mobile':tel,
        'scf':'ms',
        'validate_code':code,
        'validate_token':token}
session.post(url_2,headers=headers,data=data_2)