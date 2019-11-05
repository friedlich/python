import time
# timestr = "2020-10-10 10:10:10"
# t = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
print(time.strftime("%Y{y}%m{m}%d{d}%H{h}%M{m1}%S{s}").format(y='年', m='月', d='日',h="时",m1="分",s="秒"))
print(time.strftime("%Y{y}%m{m}%d{d}%H{h}%M{m1}%S{s}", time.localtime(time.time())).format(y='年', m='月', d='日',h="时",m1="分",s="秒"))

minute = 5
datetime = time.strftime('%Y{y}%m{m}%d{d} %H:%M', time.localtime(time.time() - float(minute) * 60)).format(y='年', m='月', d='日')
print(datetime)