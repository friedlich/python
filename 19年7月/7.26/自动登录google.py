from splinter.browser import Browser

with Browser() as browser:
    # Visit URL
    url = "http://www.google.com"
    browser.visit(url)
    browser.fill('q', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button
    button = browser.find_by_name('btnG')
    # Interact with elements
    button.click()
    if browser.is_text_present('splinter.readthedocs.io'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")

# 第1行是导入Browser。
# Browser是整个测试的基础，你可以把它理解为一个浏览器。
# 第3行初始化一个Browser，不加参数的话默认是firefox。
# 第4行是命令browser打开"http://google.com"。
# 第5行是命令browser使用‘splinter - python acceptance testing for web applications’填充页面中‘name’是‘q’的元素。在Google的首页中，就是那个搜索框。大家可以看一下Google首页的代码。
# 第6行是两个命令。第一个是找到‘name’属性为‘btnG’的按钮，第二个是click()也就是点击这个按钮。这个按钮就是Google的搜索按钮。
# 第8行是判断页面中是否有‘splinter.cobrateam.info’这个字符串，因为上一步点击了搜索按钮，所以这里搜索的就是跳转之后的页面。当然，大家不用担心网速慢会判断出错，splinter会等页面载入完成再进行下一步的操作。
# 第13行是删除browser。


