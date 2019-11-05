# 标准库一般意味着最原始最基础的功能，第三方库很多是去调用标准库中封装好了的操作函数。比如schedule，
# 就是用time和datetime来实现的。
# 而对于我们需要的定时功能，time和datetime当然能实现，但操作逻辑会相对复杂；而schedule就是可以直接解决定时功能，
# 代码比较简单，这是我们选择schedule的原因。
# 这并不意味着time和datetime比schedule差，只是这个项目场景下，我们倾向于调用schedule

import schedule
import time
#引入schedule和time

def job():
    print("I'm working...")
#定义一个叫job的函数，函数的功能是打印'I'm working...'

schedule.every(10).minutes.do(job)       #部署每10分钟执行一次job()函数的任务
schedule.every().hour.do(job)            #部署每×小时执行一次job()函数的任务
schedule.every().day.at("10:30").do(job) #部署在每天的10:30执行job()函数的任务
schedule.every().monday.do(job)          #部署每个星期一执行job()函数的任务
schedule.every().wednesday.at("13:15").do(job)#部署每周三的13：15执行函数的任务

while True:
    schedule.run_pending()
    time.sleep(1)    
#13-15都是检查部署的情况，如果任务准备就绪，就开始执行任务。
# 第15-17行是一个while循环，是去检查上面的任务部署情况，如果任务已经准备就绪，就去启动执行。
# 其中，第15行的time.sleep(1)是让程序按秒来检查，如果检查太快，会浪费计算机的资源。