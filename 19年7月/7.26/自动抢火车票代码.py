from splinter.browser import Browser
from time import sleep
import traceback


class Buy_Tickets(object):
    # 定义实例属性，初始化
    def __init__(self, username, passwd, order, passengers, dtime, starts, ends):
        self.username = username
        self.passwd = passwd
        # 车次，0代表所有车次，依次从上到下，1代表所有车次，依次类推
        self.order = order
        # 乘客名
        self.passengers = passengers
        # 起始地和终点
        self.starts = starts
        self.ends = ends
        # 日期
        self.dtime = dtime
        # self.xb = xb
        # self.pz = pz
        self.login_url = 'https://kyfw.12306.cn/otn/login/init'
        self.initMy_url = 'https://kyfw.12306.cn/otn/index/initMy12306'
        self.ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init'
        self.driver_name = 'chrome'
        self.executable_path = 'C:\Python36\Scripts\chromedriver.exe'
    # 登录功能实现
    def login(self):
        self.driver.visit(self.login_url)
        self.driver.fill('loginUserDTO.user_name', self.username)
        # sleep(1)
        self.driver.fill('userDTO.password', self.passwd)
        # sleep(1)
        print('请输入验证码...')
        while True:
            if self.driver.url != self.initMy_url:
                sleep(1)
            else:
                break
    # 买票功能实现
    def start_buy(self):
        self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
        #窗口大小的操作
        self.driver.driver.set_window_size(700, 500)
        self.login()
        self.driver.visit(self.ticket_url)
        try:
            print('开始购票...')
            # 加载查询信息
            self.driver.cookies.add({"_jc_save_fromStation": self.starts})
            self.driver.cookies.add({"_jc_save_toStation": self.ends})
            self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
            self.driver.reload()
            count = 0
            if self.order != 0:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text('查询').click()
                    count += 1
                    print('第%d次点击查询...' % count)
                    try:
                        self.driver.find_by_text('预订')[self.order-1].click()
                        sleep(1.5)
                    except Exception as e:
                        print(e)
                        print('预订失败...')
                        continue
            else:
                while self.driver.url == self.ticket_url:
                    self.driver.find_by_text('查询').click()
                    count += 1
                    print('第%d次点击查询...' % count)
                    try:
                        for i in self.driver.find_by_text('预订'):
                            i.click()
                            sleep(1)
                    except Exception as e:
                        print(e)
                        print('预订失败...')
                        continue
            print('开始预订...')
            sleep(1)
            print('开始选择用户...')
            for p in self.passengers:

                self.driver.find_by_text(p).last.click()
                sleep(0.5)
                if p[-1] == ')':
                    self.driver.find_by_id('dialog_xsertcj_ok').click()
            print('提交订单...')
            # sleep(1)
            # self.driver.find_by_text(self.pz).click()
            # sleep(1)
            # self.driver.find_by_text(self.xb).click()
            # sleep(1)
            self.driver.find_by_id('submitOrder_id').click()
            sleep(2)
            print('确认选座...')
            self.driver.find_by_id('qr_submit_id').click()
            print('预订成功...')
        except Exception as e:
            print(e)




if __name__ == '__main__':
    # 用户名
    username = 'xxxx'
    # 密码
    password = 'xxx'
    # 车次选择，0代表所有车次
    order = 2
    # 乘客名，比如passengers = ['丁小红', '丁小明']
    # 学生票需注明，注明方式为：passengers = ['丁小红(学生)', '丁小明']
    passengers = ['丁彦军']
    # 日期，格式为：'2018-01-20'
    dtime = '2018-01-19'
    # 出发地(需填写cookie值)
    starts = '%u5434%u5821%2CWUY' #吴堡
    # 目的地(需填写cookie值)
    ends = '%u897F%u5B89%2CXAY' #西安

    # xb =['硬座座'] 
    # pz=['成人票']


    Buy_Tickets(username, password, order, passengers, dtime, starts, ends).start_buy()



# 首先介绍一下splinter使用：

# splinter.brower是一个开源工具，通过Python自动化测试ｗｅｂ，通过电脑自动操作网页。

# Splinter模块是python egg，下载当然很简单，安装： pip install splinter

# 同时还需要浏览器的驱动，Splinter的Browser类默认优先调用的驱动是firefox，所以用chrome的话需要在初始化Browser时候指定driver_name="chrome"参数，建议都明确指定浏览器！

# 注意：Chrome的驱动chromedriver，注意版本要对应，不然基本上会有unknown error，打不开浏览器

# splinter.brower基础知识：

# 创建一个Browser实例，就会打开相应的浏览器。
# visit(url): 故名思议，访问指定网站
# findbyid("控件的id").first: 根据控件的属性id找到控件，一般控件都有独立唯一的id。不然，Splinter api还提供byname,byid,by_tag等方法！first表示返回第一次找到的控件。
# fill("要填充的内容"): 用指定的内容填充相应控件
# 控件是指对数据和方法的封装。控件可以有自己的属性和方法，其中属性是控件数据的简单访问者，方法则是控件的一些简单而可见的功能、控件创建过程包括设计、开发、调试（就是所谓的3Ds开发流程,即Design、Develop、Debug）工作， 然后是控件的使用。
# 设计控件是一项繁重的工作。自行开发控件与使用控件进行可视化程序开发存在着极大的不同，要求程序员精通面向对象程序设计。创建控件的最大意义在于封装重复的工作，其次是可以扩充现有控件的功能。
# click(): 点击控件
# 登录后，browser.cookies.all()中保存了本次登录的cookie信息（dict类型），可以打印出来或者保存下次使用
# quit_browser(browser)函数: 要求用户交互输入q再退出。否则，程序跑完之后就直接退出了，释放Browser的实例，调用quit()方法，浏览器也就关闭了。
# reload() 方法用于重新加载当前文档



# 实现思路：

# 首先我们需要登陆１２３０６网站，登录时需要输入用户名与密码，然后需要输入蛋疼的验证码，然后选择起、始站，时间，车次类型，点击查询，再选择车次，乘客，提交订单。如果按照这样的手动操作下来，票早已经没有了

# 备注：加粗字体都是需要购买火车票的属性

# 实现目标：

# 整个流程全自动，自动登陆，自动查询，自动订单，自动提交订单（ (暂时不实现自动点击验证码，验证码成功几率比较低）