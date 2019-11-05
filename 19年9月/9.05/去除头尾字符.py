# Python中有三个去除头尾字符、空白符的函数，它们依次为:
# strip： 用来去除头尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
# lstrip：用来去除开头字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)
# rstrip：用来去除结尾字符、空白符(包括\n、\r、\t、' '，即：换行、回车、制表符、空格)

str = ' ab cd '
print(str)
print(str.strip())  # 删除头尾空格
print(str.lstrip())  # 删除开头空格
print(str.rstrip())  # 删除结尾空格

str2 = '1a2b12c21'
print(str2)
print(str2.strip('12'))  # 删除头尾的1和2
print(str2.lstrip('12'))  # 删除开头的1和2
print(str2.rstrip('12'))  # 删除结尾的1和2
