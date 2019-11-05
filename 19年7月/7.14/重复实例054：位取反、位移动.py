# 题目 取一个整数a从右端开始的4〜7位。
# 程序分析 可以这样考虑：
# (1)先使a右移4位。
# (2)设置一个低4位全为1,其余全为0的数。可用(0<<4)
# (3)将上面二者进行&运算。
a = int(input('请输入一个数字：'))
print('a(10): ',a)
print('a(2): ',bin(a))
b = 0 
b = ~b
b = b<<4
b = ~b
print('b(10): ',b)
print('b(2): ',bin(b))
c = a>>4
print('c(10): ',c)
print('c(2): ',bin(c))
d = b&c
print('d(10): ',d)
print('d(2): ',bin(d))