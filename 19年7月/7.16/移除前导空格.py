# 字符串中的前导空格就是出现在字符串中第一个非空格字符前的空格。我们使用方法Istrip()可以将它从字符串中移除。
print('b'+'  Data123   ')
print('b'+'  Data123   '.lstrip())
# 最初的字符串当中既有前导字符也有后缀字符，调用Istrip()去除了前导空格，如果我们想去除后缀空格，可以使用rstrip()方法。
print('Data123     '+'a')
print('Data123     '.rstrip()+'a')
print('b'+'  Data123   '.strip()+'a')