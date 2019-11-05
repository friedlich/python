# 迭代器是访问集合元素的一种方式。迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
# 迭代器只能往前不会后退。我们使用inter()函数创建迭代器。
odds=iter([1,2,3,4,5])
#每次想获取一个对象时，我们就调用next()函数
print(next(odds))
print(next(odds))
# print(odds.next()) #attributeError:'list_iterator'对象没有属性'next'