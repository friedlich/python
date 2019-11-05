# （0）. 选择题库。

# 写这个程序，要用到requests模块。
# 先用requests下载链接，再用res.json()解析下载内容。
# 让用户选择想测的词库，输入数字编号，获取题库的代码。

# 提示：记得给input前面加一个int()来转换数据类型



import requests

link = requests.get('https://www.shanbay.com/api/v1/vocabtest/category/')
#先用requests下载链接。
js_link = link.json()
#解析下载得到的内容。
bianhao = int(input('''请输入你选择的词库编号，按Enter确认
1，GMAT  2，考研  3，高考  4，四级  5，六级
6，英专  7，托福  8，GRE  9，雅思  10，任意
>'''))
#让用户选择自己想测的词库，输入数字编号。int()来转换数据类型