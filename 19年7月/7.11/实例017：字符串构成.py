# 题目 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 程序分析 利用 while 或 for 语句,条件为输入的字符不为 ‘\n’。
string = input('输入字符串：')
alp = 0
dig = 0
spa = 0
oth = 0 
for i in range(len(string )):
    if string[i].isalpha():
        alp += 1
    elif string[i].isdigit():
        dig += 1
    elif string[i].isspace():
        spa += 1
    else:
        oth += 1
print('alpha:',alp)
print('digit',dig)
print('space',spa)
print('other:',oth)

#!/usr/bin/python
str = "this";  # No space & digit in this string
print(str.isalpha())
str = "this is string example....wow!!!";
print(str.isalpha())

# 中文的汉字会被 isalpha 判定为 True：
#!/usr/bin/python
# -*- coding: UTF-8 -*-
s = u"中国"
print(s.isalpha())  # True
# 如果想区分中文和英文可以使用 unicode。中文的范围为：['/u4e00'，'/u9fa5']。判断是否是全英文： 
#!/usr/bin/python
# -*- coding: UTF-8 -*-
s = u"中国"
t = u"english"
print(s.encode( 'UTF-8' ).isalpha())  # False
print(s.encode( 'UTF-8' ))
print(t.encode( 'UTF-8' ).isalpha())
print(t.encode( 'UTF-8' ))
# 判断是否是全数字：
s = '666 '
print(s.encode( 'UTF-8' ).isdigit())
