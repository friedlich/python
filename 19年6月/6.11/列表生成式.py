# zip() 将对象中对应的元素打包成个个元组，然后返回由一这些元组组成的列表。

# res = lambda t1,t2 : 列表    
# lambda本身是个函数，冒号前是参数，冒号后是返回值
# lambda是匿名函数，赋值给一个变量，变量名就相当于函数名
# 这句话相当于
# def res(t1,t2):
#  return 列表
#完全翻译过来就是
def res(t1,t2):
    zip1 = zip(t1,t2)
    print(zip1)
    l1 = []
    for i,j in zip1:
        print({i,j})
        l1.append({i,j})
    return l1

t1 = ('a','b')
t2 = ('c','d')
print(res(t1,t2))
# 但每次运行结果是不一致的
# 结果不一致的原因是{'a','c'}是个集合，本身没有顺序
# 直接 print({'a','c'}) 结果也会不一样
print({'a','c'})


print(type('a'))
#<class 'str'>
print(type(('a')))
#<class 'str'>

# 所以 ，这两句
# t1 = (('a'),('b'))
# t2 = (('c'),('d'))
# 可以改为
# t1 = ('a','b')
# t2 = ('c','d')

t1 = ('a','b')
t2 = ('c','d')
zz = zip(t1,t2)
print(list(zz))
#[('a', 'c'), ('b', 'd')]
# for i,j in zip(t1,t2)  相当于
# for i,j in [('a', 'c'), ('b', 'd')]
# 列表里有两个元素，循环两次
# 第一次  i,j =('a', 'c')
# 第二次  i,j = ('b', 'd')

# 相当于
l1 = []
for i,j in  [('a', 'c'),('b', 'd')]:
    l1.append({i,j}) 
print(l1)

