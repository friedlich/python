import requests

def get_picture():
    url = "https://h5.ele.me/restapi/eus/v3/captchas"
    param = {"captcha_str":input("手机号码")}
    res = requests.get(url,params=param).json()["captcha_image"]
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get(res)
    time.sleep(5)



get_picture()