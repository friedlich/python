import re
content = 'To be or not to be,that is a question'
print(re.findall('\w{1,30}', content))
# 这一行中的\w 表示一个字母或者_，{1,30}表示\w 出现1 次到 30 次之间，只要一个单词的长度在 1-30 之间就能被匹配出来
print( re.findall('\w+', content))

content = '点赞数：12'
print(re.findall('\d{1,10}', content))
print(re.findall('\d+', content))