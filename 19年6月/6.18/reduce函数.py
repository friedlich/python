# reduce()函数和map()函数都是python中的高阶函数，充分的体现了大蟒的特点，和可迭代的特性。

# reduce()接受两个参数：
# 第一个参数是一个函数，第二个参数是一个可以迭代的类型（Iterable） 
# 第一个参数的函数也必须接受两个参数，reduce会把函数的返回值与序列的下一个元素继续传入函数做计算

# reduce 将函数得到的结果继续当做参数传入到函数中去
from functools import reduce
def add(x,y):
    return x*y
print(reduce(add,range(1,5)))

# 在python 3.0.0.0以后, reduce已经不在built-in function里了, 要用它就得from functools import reduce
from functools import reduce
e = reduce(lambda a,b:'{},{}'.format(a,b), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(e)
# reduce() 函数会对参数序列中元素进行累积。
# 函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给 reduce 中的函数 function（有两个参数）先对
# 集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

# python中的reduce内建函数是一个二元操作函数，他用来将一个数据集合（链表，元组等）中的所有数据进行下列操作：用
# 传给reduce中的函数 func()（必须是一个二元操作函数）先对集合中的第1，2个数据进行操作，得到的结果再与第三个数
# 据用func()函数运算，最后得到一个结果。
