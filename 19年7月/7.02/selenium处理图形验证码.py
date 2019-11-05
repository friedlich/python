import requests,time
from selenium import webdriver

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


driver = webdriver.Chrome()

driver.get('https://h5.ele.me/login/')
time.sleep(2)

tel = driver.find_elements_by_class_name('MessageLogin-FsPlX')[0].find_element_by_tag_name('input')
tel.send_keys('19921876546')
button1 = driver.find_element_by_class_name('CountButton-3e-kd')
button1.click()
time.sleep(2)

captcha1 = driver.find_element_by_class_name('MessageLogin-iYvWA').find_element_by_tag_name('input')
captcha1.send_keys(input('请填写图形验证码：'))
button = driver.find_element_by_class_name('Captcha-ok_2tFUQc1')
button.click()
time.sleep(2)

captcha2 = driver.find_elements_by_class_name('MessageLogin-FsPlX')[1].find_element_by_tag_name('input')
captcha2.send_keys(input('请填写手机验证码：'))
button2 = driver.find_element_by_class_name('SubmitButton-2wG4T')
button2.click()
time(2)




