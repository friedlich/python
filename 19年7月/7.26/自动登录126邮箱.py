# 这里，我给出自动登录126邮箱的案例。难点是要找到页面的账户、密码、登录的页面元素，这里需要查看126邮箱登录页面的源码，
# 才能找到相关控件的id.
#    例如:输入密码，密码的文本控件id是pwdInput.可以使用browser.find_by_id()方法定位到密码的文本框，
#    接着使用fill()方法，填写密码。至于模拟点击按钮，也是要先找到按钮控件的id,然后使用click()方法。
# 由于代码较简单，我就只在代码中给出注解说明工作原理。

#coding=utf-8
import time
from splinter.browser import Browser
 
def splinter(url):
    browser = Browser('chrome')
    #login 126 email websize
    browser.visit(url)
    #wait web element loading
    time.sleep(5)
    #fill in account and password
    browser.find_by_id('idInput').fill('xxxxxx')
    browser.find_by_id('pwdInput').fill('xxxxx')
    #click the button of login
    browser.find_by_id('loginBtn').click()
    time.sleep(8)
    #close the window of brower
    browser.quit()
 
if __name__ == '__main__':
    websize3 ='http://www.126.com'
    splinter(websize3)

