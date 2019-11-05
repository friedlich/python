# 对于这个问题，我们可以使用isalnum()方法。
print('DATA123'.isalnum())
True
print('DATA123!'.isalnum())
False
# 我们还可以用其它一些方法：

print('123'.isdigit())#检测字符串是否只由数字组成
True
print('123'.isnumeric())#只针对unicode对象
True

print('data'.islower())#是否都为小写
True
print('Data'.isupper())#是否都为大写
False