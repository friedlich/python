import re
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import time
from config import *
import pymongo

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

chromedriver_path = r'C:\Users\asus\AppData\Local\Programs\Python\Python36\chromedriver.exe'  # 其实我已经配好环境变量了
chrome_options = Options()  # 实例化Option对象
# options = webdriver.ChromeOptions() # 这也是一种方式，在没有导入Options的情况下可以这样
# chrome_options.add_argument('--headless')  # 把Chrome浏览器设置为静默模式
browser = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)  # 设置引擎为Chrome，在后台默默运行
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS) # 对PhantomJS的Selenium支持已被弃用，请使用无头
wait = WebDriverWait(browser, 10)  # 超时时长为10s

browser.set_window_size(1400, 900)


# 登录淘宝
def login():
    url = 'https://login.taobao.com/member/login.jhtml'
    # 打开网页
    browser.get(url)

    # 等待 密码登录选项 出现
    password_login = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
    password_login.click()

    # 等待 微博登录选项 出现
    weibo_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
    weibo_login.click()

    # 等待 微博账号 出现
    weibo_user = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.username > .W_input')))
    weibo_user.send_keys(weibo_username)

    # 等待 微博密码 出现
    weibo_pwd = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.password > .W_input')))
    weibo_pwd.send_keys(weibo_password)

    # 等待 登录按钮 出现
    submit = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_tip > a > span')))
    submit.click()

    # 直到获取到淘宝会员昵称才能确定是登录成功
    # taobao_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))
    # taobao_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.tbh-member J_Module > div.member > div.member-bd > span.member-nick-info > .J_MemberNick member-nick')))

    # 输出淘宝昵称
    # print(taobao_name.text)


def search():
    print('正在搜索')
    try:
        login()
        print('登陆成功')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        # 哥哥我笑了，居然是这里的问题，这个选择器的问题，J_SearchForm > button这他妈我自己去实操找的居然不对，感觉有点浪费时间
        # 怎么说呢，一定要学会看报错，这样可以节省很多时间
        input.send_keys(KEYWORD)
        time.sleep(2)
        submit.click()
        time.sleep(2)
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        get_products()
        return total.text
    except TimeoutException:
        return search()


def next_page(page_number):
    print('正在翻页', page_number)
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
        get_products()
    except TimeoutException:
        next_page(page_number)


def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)


def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('存储到MONGODB成功', result)
    except:
        print('存储到MONGODB失败', result)


def main():
    try:
        total = search()
        total = int(re.compile('(\d+)').search(total).group(1))
        print(total)
        for i in range(5, 7):
            next_page(i)
    except Exception:
        print('出错啦')
    finally:
        browser.close()


if __name__ == "__main__":
    weibo_username = "19921876546"  # 改成你的微博账号
    weibo_password = "252272?q"  # 改成你的微博密码

    main()
