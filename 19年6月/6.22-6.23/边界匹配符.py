import re
content = 'https://www.zhihu.com'
content1 = '/question/62749917/answer/576934857'
print(re.findall('^http.*', content))
# 这一行的^http 表示匹配 content 的首部是 http 的内容，后面的.表示一个除换行符\n 以外的所有字符，*表示重复 0 次或
# 无限多次，.*放在一起就是匹配除换行符以外的任意字符无限多次，这两个字符经常放在一起用
print(re.findall('^http.*', content1))


import re
content = 'https://www.zhihu.com/shiyue.png'
content1 = 'https://www.zhihu.com'
print(re.findall('.*png$', content))
# 这一行的.*和之前一样，表示 png 前面可以有除换行符之外的任意字符，png$表示匹配 content 以 png 结尾的内容。
print(re.findall('.*png$', content1))