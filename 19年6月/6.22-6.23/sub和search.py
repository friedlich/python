import re
content = '点赞数：12'
result_match = re.match('\d', content)
result_search = re.search('\d', content)
print(result_match)
print(result_search)
print(result_search.group())
# 可以看到，使用 match 方法，会从 content 的开头去匹配\d，没有匹配到就直接返回 None了。
# 而 search 方法也是从头开始匹配，只要匹配到有一个字符符合\d，就直接返回了，不会继续往下匹配。
# search方法返回的也是一个SRE_Match对象，和match方法的取值是一样的，用group()。

## 接下来，我们来看下 sub 方法，这个方法能实现的功能是匹配出结果并替换掉内容
content = 'python PHP java c javascript java php'
print(re.sub('php', 'python', content))
print(type(re.sub('php', 'python', content)))
# sub 方法的第一个参数是正则表达式，第二个参数是替换之后的字符串，第三个参数是目标字符串
print(re.sub('php', 'python', content, flags=re.I))
# 这一行的 flags=re.I 表示的是匹配模式，re.I 表示第一个参数不区分大小写
# 还有一种常用的匹配模式 re.S，在这种模式下.表示任意字符。普通模式下.表示除换行符外的任意字符
print(re.sub('php', 'python', content, count=1, flags=re.I))
# 这里的 re.sub 的第四个参数count=1 表示无论匹配到多少个 php，最多只将第 1 个 php 替换成 python，count=8 的话就表示
# 无论匹配到多少个 php，最多只将前 8 个 php 替换成 python

### 接下来，我们来看下 sub 方法设计的精妙之处，就是 sub 的第二个参数可以是一个函数。
# 精妙之处在哪呢，就在于当你拿到匹配结果的时候，不一定要将它替换成固定的字符串，你可以传递一个函数，在函数中对匹配结果
# 进行逻辑处理，这样主动权就交到了用户手上，用户可以随便处理
def judge(value):
    print(type(value))
    value = value.group()
    print(type(value))
# 用 group 方法获取到匹配结果，以下逻辑是对 value 进行逻辑判断
    if int(value) < 60:
        return '不及格'
    elif int(value) < 80:
        return '中'
    elif int(value) < 90:
        return '良'
    else:
        return '优'

content = '小明：59 小红：66 小白：83 小绿：98 小王：100'
result = re.sub('\d+', judge, content)
# 这里 sub 的第二个参数就是一个函数 judge，第一个参数匹配到的结果会作为 value 传递进 judge 函数中，从而在 judge 
# 中可以对他进行判断，函数的返回值将会替换掉匹配结果。
print(result)
# 这个 sub 方法的使用并不难，可有一点值得我们去学习，那就是将函数作为一个参数传递到另一个函数中，这是一种非常经典的设计
# ，值得大家去思考学习。