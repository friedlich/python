# 方法2：map+匿名函数

# lambda argument_list: expression
# 其中，lambda是Python预留的关键字，argument_list和expression由用户自定义
# 这里的argument_list是参数列表，它的结构与Python中函数(function)的参数列表是一样的 
# 这里的expression是一个关于参数的表达式。表达式中出现的参数需要在argument_list中有定义，并且表达式只能是单行的
# 这里的lambda argument_list: expression表示的是一个函数。这个函数叫做lambda函数

info = [0,1,2,3,4,5,6,7,8,9]
a = list(map(lambda x: x+1, info))
print(a)
for i in a:
    print(i)

add=lambda x, y: x+y
print(add(1,2))

b = list((filter(lambda x: x % 3 == 0, [1, 2, 3])))
print(b)
b1 = (filter(lambda x: x % 3 == 0, [1, 2, 3]))
print(b1)

c = sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda keys: abs(5-keys))
print(c)

d = list(map(lambda a:'{}'.format(a), [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(d)

# 在python 3.0.0.0以后, reduce已经不在built-in function里了, 要用它就得from functools import reduce
from functools import reduce
e = reduce(lambda a,b:'{},{}'.format(a,b), [1, 2, 3, 4, 5, 6, 7, 8, 9])
f = reduce(lambda a,b:'{} {}'.format(a,b), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(e)
print(f)
# reduce() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）
# 先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

