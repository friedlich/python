# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list,tuple,dict,set,str等
# 一类是generator，包括生成器和带yield的generator function
# 这些可以直接作用于for 循环的对象统称为可迭代对象：Iterable
# 可以使用isinstance()判断一个对象是否为可Iterable对象
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
print(isinstance((x for x in range(10)),Iterable))
print(isinstance(100,Iterable))
# 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
# 直到最后抛出StopIteration错误表示无法继续返回下一个值了。

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象
from collections import Iterator
print(isinstance((x for x in range(10)),Iterator))
print(isinstance([],Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
# 生成器都是 Iterator 对象，但 list 、 dict 、 str 虽然是 Iterable（可迭代对象） ，却
# 不是 Iterator（迭代器）
# 把list、dict、str等Iterable变成Iterator可以使用 iter() 函数：
print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter('abc'),Iterator))
# 你可能会问，为什么 list 、 dict 、 str 等数据类型不是 Iterator ？
# 这是因为Python的 Iterator 对象表示的是一个数据流，Iterator对象可以被 next()
# 函数调用并不断返回下一个数据，直到没有数据时抛出 StopIteration 错误。可以
# 把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不
# 断通过 next() 函数实现按需计算下一个数据，所以 Iterator 的计算是惰性的，只
# 有在需要返回下一个数据时它才会计算。
# Iterator 甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远
# 不可能存储全体自然数的。

# 1 s='hello'
# 2 l=[1,2,3,4]
# 3 t=(1,2,3)
# 4 d={'a':1}
# 5 set={1,2,3}
# 6 f=open('a.txt')
# 7
# 8 s='hello'     #字符串是可迭代对象，但不是迭代器
# 9 l=[1,2,3,4]     #列表是可迭代对象，但不是迭代器
# 10 t=(1,2,3)       #元组是可迭代对象，但不是迭代器
# 11 d={'a':1}       #字典是可迭代对象，但不是迭代器
# 12 set={1,2,3}     #集合是可迭代对象，但不是迭代器
# 13 # *************************************
# 14 f=open('test.txt') #文件是可迭代对象，是迭代器
# 15
# 16 #如何判断是可迭代对象，只有__iter__方法，执行该方法得到的迭代器对象。
# 17 # 及可迭代对象通过__iter__转成迭代器对象
# 18 from collections import Iterator #迭代器
# 19 from collections import Iterable #可迭代对象
# 20
# 21 print(isinstance(s,Iterator))     #判断是不是迭代器
# 22 print(isinstance(s,Iterable))       #判断是不是可迭代对象
# 23
# 24 #把可迭代对象转换为迭代器
# 25 print(isinstance(iter(s),Iterator))
# 26 注意：文件的判断
# 27
# 28 f = open('housing.csv')
# 29 from collections import Iterator
# 30 from collections import Iterable
# 31
# 32 print(isinstance(f,Iterator))
# 33 print(isinstance(f,Iterable))
# 34
# 35 True
# 36 True