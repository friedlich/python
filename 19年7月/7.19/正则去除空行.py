# python用正则表达式去除空行
# 假如有如下字符串
# str="aaa\n\nbbb\n\n\n"
# print re.sub('正则表达式','',str)
# 用怎样的正则表达式才能把空行去掉，输出
# aaa
# bbb
# 这样的格式 
str="aaa\n\nbbb\n\n\n"
str1='ccc\n\n\n\n\n\nddd\n\n\n\ndet'
# print(str)
import re
str="aaa\n\nbbb\n\n\n"
# print(re.sub('[\r\n\f]','\n',str)) # \s表示该位置上是不可见字符（空格、制表符\t、垂直制表符\v、回车符\r、换行符\n、换页符\f），即匹配成功
# print(re.sub('[\r\n\f]{2,}','\n',str)) 
print(re.sub('[\n]{2,}','\n',str)) # {3,8}表示{3}前面的一个字符出现 3-8 次
print(re.sub('[\n]{2,}','\n',str1))