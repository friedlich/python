import re
import time
import locale
locale.setlocale(locale.LC_CTYPE, 'chinese')
ptime = '52分钟前 '
if re.match('\d+分钟前', ptime.strip()):
    minute = re.match('(\d+)', ptime.strip()).group(1)
    print(minute)
    datetime = time.strftime('%Y年%m月%d日', time.localtime())
    # datetime = time.strftime('%Y年%m月%d日 %H:%M', time.localtime(time.time() - float(minute) * 60))
    print(datetime)