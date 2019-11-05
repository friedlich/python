# 题目 时间函数举例1。
# 程序分析 无。
if __name__ == '__main__':
    import time
    print(time.ctime(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))

# Python time gmtime() 函数将一个时间戳转换为UTC时区（0时区）的struct_time，可选的参数sec表示从1970-1-1以来的秒数。
# 其默认值为time.time()，函数返回time.struct_time类型的对象。（struct_time是在time模块中定义的表示时间的对象）。
# gmtime()方法语法：
# time.gmtime([ sec ])
# 参数 sec -- 转换为time.struct_time类型的对象的秒数。
# 返回值 该函数没有任何返回值。
import time
print('time.gmtime() : {}'.format(time.gmtime()))

# Python time ctime() 函数把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。 如果参数未给或者为None的时候
# ，将会默认time.time()为参数。它的作用相当于 asctime(localtime(secs))。
# ctime()方法语法：
# time.ctime([ sec ])
# 参数 sec -- 要转换为字符串时间的秒数。
# 返回值 该函数没有任何返回值。
from time import *
print("time.ctime() : {}".format(ctime()))
print(asctime(localtime()))

## 
# localtime方法，该方法的参数为我们刚刚所说的1970年到目前为止的秒数，返回值为一个叫struct_time结构体，
# 如果不懂什么叫结构体，没关系，也可以理解为localtime方法返回一个struct_time对象。
# 要获得一个易于理解的数据，常见的asctime类型，进行时间格式化
