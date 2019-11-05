import re
content = '发布于 2018/12/23'
print(re.findall('.*?(\d.*\d)', content))
# 这一行的.*表示匹配除换行符外的任意字符，？表示非贪婪匹配，这个放在后面讲
# (\d.*\d)表示一个组，以数字开头，以数字结尾，.*表示中间可以是除换行以外的任意字符
# 最终返回的结果就是括号内匹配到的结果。
print(re.findall('.*?\d.*\d', content))
# 因为 python 默认会在正则表达式首尾各添加一个括号  
print(re.findall(('.*?\d.*\d'), content))

content = '发布于 2018/12/23,发布人：十月'
print(re.findall('.*?(\d.*\d).*：(.*)', content))
# 所以上述正则表达式的意思是：以除换行符以外的任意字符开头，直到遇见第一个组，以数字开头，以数字结尾，这样就能匹配到发布时
# 间 2018/12/23，然后又是除换行符外的任意字符，直到遇见：进入第二个组，分号后面所有的内容构成第二个组，匹配到发布人十月

### match方法
result = re.match('.*?(\d.*\d).*：(.*)', content)
print(result)
print(result.group())
# 得到的结果是'发布于 2018/12/23,发布人：十月'，该方法默认是 result.group(0)
# 前文说过 re.match('.*?(\d.*\d).*：(.*)', content)等价于re.match('(.*?(\d.*\d).*：(.*))', content)
# result.group(0)获取的内容就是最外层的括号匹配的内容。
print(result.group(1))
print(result.group(2))
print(result.groups())
content = '评论数：12'
print(re.match('\d', content))
# 得到的结果是 None，如果直接 print(result.group())是会报错的。原因在于 match 方法是从 content 第一个字符开始去
# 匹配\d，如果未匹配到，直接就返回 None。这里因为content 第一个字符不是数字，所以直接返回 None
