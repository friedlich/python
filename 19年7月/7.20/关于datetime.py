import datetime
# print(datetime.datetime('7-20', "%m-%d")) # TypeError：需要一个整数（得到类型str）
# print(type(datetime.strptime(7-20, "%m-%d")))
print(datetime.datetime.strptime('7-20', "%m-%d"))
print(type(datetime.datetime.strptime('7-20', "%m-%d")))
print(datetime.datetime(2019,7,20))
print(type(datetime.datetime(2019,7,20)))