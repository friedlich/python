import time
def consumer(name):
    print("%s 准备学习啦!"%name)
    while True:     
        lesson = yield # 这里的yield的初始值是0，可以在下面的range（）里面改，这也是赋值
        # lesson = '上数学课'
        print("开始[%s]了,[%s]老师来讲课了!"%(lesson,name))



def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    # 要是没这两句的话，会报错：c.send（ⅰ）TypeError：无法向刚刚启动的生成器发送非None值
    print('"同学们开始上课 了!"')
    for i in range(1,10):    
        time.sleep(1)
        print('到了两个同学')
        c.send(i)
        c2.send(i)
#     for i in ['语文','数学','英语','物理']:
#         time.sleep(1)
#         print('到了两个同学')
#         c.send(i)
#         c2.send(i)
producer('C')    


#    生成器函数：也是用def定义的，利用关键字yield一次性返回一个结果，阻
# 塞，重新开始
#    生成器表达式：返回一个对象，这个对象只有在需要的时候才产生结果

# ——生成器函数
# 为什么叫生成器函数？因为它随着时间的推移生成了一个数值队列。一般的函数
# 在执行完毕之后会返回一个值然后退出，但是生成器函数会自动挂起，然后重新
# 拾起急需执行，他会利用yield关键字关起函数，给调用者返回一个值，同时保
# 留了当前的足够多的状态，可以使函数继续执行，生成器和迭代协议是密切相关
# 的，可迭代的对象都有一个next()__成员方法，这个方法要么返回迭代的下一
# 项，要买引起异常结束迭代




