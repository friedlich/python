from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()  # 实例化Option对象
chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})  # 不加载图片,加快访问速度
browser = webdriver.Chrome(chrome_options=chrome_options)

wait = WebDriverWait(browser, 10)  # 超时时长为10s

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

def login():
    url = 'https://login.taobao.com/member/login.jhtml'

    browser.get(url)

    # 等待 密码登录选项 出现
    password_login = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static')))
    password_login.click()

    # 等待 微博登录选项 出现
    weibo_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_OtherLogin > a.weibo-login')))
    weibo_login.click()

    # 等待 微博账号 出现
    weibo_user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(2) > div > input')))
    weibo_user.send_keys(weibo_username)

    # 等待 微博密码 出现
    weibo_pwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(3) > div > input')))
    weibo_pwd.send_keys(weibo_password)

    # 等待 登录按钮 出现
    submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(7) > div:nth-child(1) > a > span')))
    submit.click()

if __name__ == "__main__":
    weibo_username = "19921876546"  # 改成你的微博账号
    weibo_password = "252272?q"  # 改成你的微博密码

    login()

