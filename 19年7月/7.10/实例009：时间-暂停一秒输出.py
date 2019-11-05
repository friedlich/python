# 题目 暂停一秒输出。
# 程序分析 使用 time 模块的 sleep() 函数。
import time
for i in range(4):
    print(time.time())
    print(int(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(str(int(time.time()))[-2:])
    time.sleep(1)

### 用python获得当前日期和时间
# 第一步要做的就是从1970纪元后到目前为止度过的秒数（浮点类型）,其实想要获得这个秒数，只有一个方法，就是通过time模块内的time方法来获得。即time.time()
# 但是，time.time返回的这个高精度浮点数我们并不能准确的得到我们想要的当前时间。我们只知道这是从1970到目前为止已经过了多少秒。
# 这里我们还需要使用一个方法来把秒数变成当前的时间戳。这时我们就要用到另外一个方法，localtime方法，该方法的参数为我们刚刚所说的
# 1970年到目前为止的秒数，返回值为一个叫struct_time结构体，如果不懂什么叫结构体，没关系，也可以理解为localtime方法返回一个
# struct_time对象。
print(time.localtime(time.time()))
# 可以看到localtime方法的返回结果，从单词的字面上我们也能大概了解到：
# 前缀tm为time，year为年份，mon为月份，mday为日，hour为时，min为分，sec为秒等等
# 要获得一个易于理解的数据。常见的asctime类型，例如显示结果如Wed Feb 13 15:46:11 2018 如果小伙伴常用Linux对这种类型显然不会
# 陌生，在linux上，我们使用date命令，不进行时间格式化的话，就会输出这种形式的时间。例如小编这里虚拟机内的linux，运行date的输出结果如图。
# 格式为:星期几 月份 日数 时:分:秒 年份
# 注意的是，在linux上的date默认会输出时间区域，例如默认的美国时间EDT，或者修改为我们大陆的北京时间CTS。
# 这里提供两种方法进行struct_time数据格式化。
# 第一种就是第4步讲述的asctime格式，我们调用time模块内的asctime方法即可，参数为struct_time对象数据，返回字符串，即asctime格式当前日期时间。
print(time.asctime(time.localtime(time.time())))
# 'Wed Apr  4 20:27:15 2018' ,翻译成中文是：星期三 四月 4 20:27:15 2018
# 还有一个数据格式化的方法是time模块内提供的strftime方法。str time.strftime(格式转化字符,时间戳)  格式转化字符如下：
# %y 两位数的年份表示（00-99）%Y 四位数的年份表示（000-9999）%m 月份（01-12）%d 月内中的一天（0-31）%H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）%M 分钟数（00=59）%S 秒（00-59）%a 本地简化星期名称 %A 本地完整星期名 %b 本地简化的月份名称
# %B 本地完整的月份名称 %c 本地相应的日期表示和时间表示 %j 年内的一天（001-366）%p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始 %w 星期（0-6），星期天为星期的开始 %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示 %X 本地相应的时间表示 %Z 当前时区的名称 %% %号本身
# 这里常用的小编就进行了加粗，其实常用的就是这几个。一定要记住的是：
### %Y = 年，%m = 月，%d = 日，%H = 24制时，%M = 分，%S = 秒。
# 例如我们可以获得当前时间和日期，然后获得当前是一年中的第几天，然后获得当前的时区
# print(time.strftime("当前日期:%Y年%m月%d日",time.localtime(time.time())))
print(time.strftime("%Y-%m-%d",time.localtime(time.time())))
#获得当前日期
print(time.strftime("%H:%M:%S",time.localtime(time.time())))
#获得当前时间
print(time.strftime(" %Y %W %j %a %p %I %x %Z",time.localtime(time.time())))
# 代码只能在python3中有效运行，python2需要使用print输出（否则中文会变成16进制字符）。