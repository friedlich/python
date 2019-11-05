# eval()函数十分强大，官方demo解释为：将字符串str当成有效的表达式来求值并返回计算结果：
s='8*8'
print(s)
print(eval(s))
print(eval('2+5*4'))
x = 1
y = 4
print(eval('x+y'))
print(eval('98.9'))
print(eval('9.9\n'))
print(eval('9.9\n\t\r  \t\r\n'))

### 可以把list,tuple,dict和string相互转化：
l = "[2,3,4,5]"
ll=eval(l)
print(ll)
print(type(ll))
d="{'name':'python','age':20}"
dd=eval(d)
print(type(dd))
print(dd)
t='(1,2,3)'
print(type(t))
print(t)
tt=eval(t)
print(type(tt))
print(tt)

# eval()函数功能强大，但也很危险，若程序中有以下语句：
s = input('please input:')
# s = raw_input('please input:')
print(eval(s))

# 下面举几个被恶意用户使用的例子：
# 1》运行程序，如果用户恶意输入：

# please input:__import__('os').system('dir')
# 则eval()之后，当前目录文件都会展现在用户前面。。。

# 2》运行程序，如果用户恶意输入：

# please input:open('data.py').read()

# 如果，当前目录中恰好有一个文件，名为data.py，则恶意用户变读取到了文件中的内容。。。

# 3》运行程序，如果用户恶意输入：

# please input:__import__('os').system('del delete.py /q')
# 如果，当前目录中恰好有一个文件，名为delete.py，则恶意用户删除了该文件。。。
# /q ：指定静音状态。不提示您确认删除。