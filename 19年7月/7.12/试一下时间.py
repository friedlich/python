import datetime
da='2019-07-12 04:23:19'
date = datetime.datetime.strptime(da,'%Y-%m-%d %H:%M:%S')
print(date)
print(type(date))