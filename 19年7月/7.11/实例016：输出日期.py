# 题目 输出指定格式的日期。
# 程序分析 使用 datetime 模块
import datetime
print(datetime.date.today())
print(datetime.date(2333,2,3))
print(datetime.date.today().strftime('%d/%m/%Y'))
day = datetime.date(1111,2,3)
day = day.replace(day.year+22)
print(day)
