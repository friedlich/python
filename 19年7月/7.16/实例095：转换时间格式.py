# 题目 字符串日期转换为易读的日期格式。
# 程序分析 看看就得了，dateutil是个第三方库。
from dateutil import parser
dt = parser.parse("Aug 28 2015 12:00AM")
print (dt)

# 背景：
# 我有很多很多的日志数据，每个日志里面都有日期字符串，我需要将其转换为datetime格式。
# 问题是，这些日志里的字符串格式五花八门，有2017-05-25T05:27:30.313292255Z，有2016-07-01T00:00:00以及其他各种我
# 还没有看到的格式。
# 开始我写了一长串的if else来判断格式，但是总有我漏掉的。
# 最后上网一查，发现dateutil.parser.parse。可以不用我们指定格式，直接将字符串转换为datetime格式。
import datetime
import dateutil.parser
def getDateTime(s):
    d = dateutil.parser.parse(s)
    return d
# 注：我试了下"19/May/2017:04:10:06 +0000" 居然失败了- -！那可能这个函数只认识数字不认得字母吧。
