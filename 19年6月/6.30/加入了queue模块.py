# 第1部分是导入模块
from gevent import monkey
#从gevent库里导入monkey模块。
monkey.patch_all()
#monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步。
import gevent,time,requests
#导入gevent、time、requests
from gevent.queue import Queue
#从gevent库里导入queue模块
#因为gevent库里就带有queue，所以我们用【from gevent.queue import Queue】就能把queue模块导入。其他模块和代码我们在讲解gevent时已经讲解过了，相信你能懂。


# 第2部分，是如何创建队列，以及怎么把任务存储进队列里
start = time.time()
#记录程序开始时间

url_list = ['https://www.baidu.com/',
'https://www.sina.com.cn/',
'http://www.sohu.com/',
'https://www.qq.com/',
'https://www.163.com/',
'http://www.iqiyi.com/',
'https://www.tmall.com/',
'http://www.ifeng.com/']

work = Queue()
#创建队列对象，并赋值给work。
for url in url_list:
#遍历url_list
    work.put_nowait(url)
    #用put_nowait()函数可以把网址都放进队列里。
# 用Queue()能创建queue对象，相当于创建了一个不限任何存储数量的空队列。如果我们往Queue()中传入参数，比如Queue(10)，则表示这个队列只能存储10个任务。
# 创建了queue对象后，我们就能调用这个对象的put_nowait方法，把我们的每个网址都存储进我们刚刚建立好的空队列里。
# work.put_nowait(url)这行代码就是把遍历的8个网站，都存储进队列里。


# 第3部分，是定义爬取函数，和如何从队列里提取出刚刚存储进去的网址。
def crawler():
    while not work.empty():
    #当队列不是空的时候，就执行下面的程序。
        url = work.get_nowait()
        #用get_nowait()函数可以把队列里的网址都取出。
        r = requests.get(url)
        #用requests.get()函数抓取网址。
        print(url,work.qsize(),r.status_code)
        #打印网址、队列长度、抓取请求的状态码。
# 这里定义的crawler函数，多了三个你可能看不懂的代码：1.while not work.empty()：；2.url = work.get_nowait()；3.work.qsize()。
# 这三个代码涉及到queue对象的三个方法：empty方法，是用来判断队列是不是空了的；get_nowait方法，是用来从队列里提取数据的；qsize方法，是用来判断队列里还剩多少数量的。


# 接在第3部分代码的后面，就是让爬虫用多协程执行任务，爬取队列里的8个网站的代码（重点看有注释的代码）
tasks_list  = [ ]
#创建空的任务列表
for x in range(2):
#相当于创建了2个爬虫
    task = gevent.spawn(crawler)
    #用gevent.spawn()函数创建执行crawler()函数的任务。
    tasks_list.append(task)
    #往任务列表添加任务。
gevent.joinall(tasks_list)
#用gevent.joinall方法，执行任务列表里的所有任务，就是让爬虫开始爬取网站。
end = time.time()
print(end-start)
# 我们创建了两只可以异步爬取的爬虫。它们会从队列里取走网址，执行爬取任务。一旦一个网址被一只爬虫取走，另一只爬虫就取不到了
# ，另一只爬虫就会取走下一个网址。直至所有网址都被取走，队列为空时，爬虫就停止工作。

