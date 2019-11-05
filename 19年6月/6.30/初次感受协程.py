from gevent import monkey
#从gevent库里导入monkey模块。
monkey.patch_all()
#monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步。
import gevent,time,requests
#导入gevent、time、requests。

start = time.time()
#记录程序开始时间。

url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']
#把8个网站封装成列表。

def crawler(url):
#定义一个crawler()函数。
    r = requests.get(url)
    #用requests.get()函数爬取网站。
    print(url,time.time()-start,r.status_code)
    #打印网址、请求运行时间、状态码。

tasks_list = [ ]
#创建空的任务列表。

for url in url_list:
#遍历url_list。
    task = gevent.spawn(crawler,url)
    #用gevent.spawn()函数创建任务。
    tasks_list.append(task)
    #往任务列表添加任务。
gevent.joinall(tasks_list)
#执行任务列表里的所有任务，就是让爬虫开始爬取网站。
end = time.time()
#记录程序结束时间。
print(end-start)
#打印程序最终所需时间。

# 第1、3行代码：从gevent库里导入了monkey模块，这个模块能将程序转换成可异步的程序。monkey.patch_all()，它的作用其实就像你的电脑有时会弹出“是否要用补丁修补漏洞或更新”一样。它能给程序打上补丁，让程序变成是异步模式，而不是同步模式。它也叫“猴子补丁”。
# 我们要在导入其他库和模块前，先把monkey模块导入进来，并运行monkey.patch_all()。这样，才能先给程序打上补丁。你也可以理解成这是一个规范的写法。

# 第5行代码：我们导入了gevent库来帮我们实现多协程，导入了time模块来帮我们记录爬取所需时间，导入了requests模块帮我们实现爬取8个网站。

# 第21、23、25行代码：我们定义了一个crawler函数，只要调用这个函数，它就会执行【用requests.get()爬取网站】和【打印网址、请求运行时间、状态码】这两个任务。

# 第33行代码：因为gevent只能处理gevent的任务对象，不能直接调用普通函数，所以需要借助gevent.spawn()来创建任务对象。
# 这里需要注意一点：gevent.spawn()的参数需为要调用的函数名及该函数的参数。比如，gevent.spawn(crawler,url)就是创建一个执行crawler函数的任务，参数为crawler函数名和它自身的参数url。

# 第35行代码：用append函数把任务添加到tasks_list的任务列表里。

# 第37行代码：调用gevent库里的joinall方法，能启动执行所有的任务。gevent.joinall(tasks_list)就是执行tasks_list这个任务列表里的所有任务，开始爬取。