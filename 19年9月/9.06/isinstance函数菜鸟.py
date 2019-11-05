# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。

# isinstance()与type()区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# 如果要判断两个类型是否相同推荐使用 isinstance()。

a = 2
print(isinstance(a, int))
print(isinstance(a, str))
print(isinstance(a, (str, int, list)))   # 是元组中的一个返回 True

# type() 与 isinstance()区别：


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))  # returns True
print(type(A()) == A)  # returns True
print(isinstance(B(), A))  # returns True
print(type(B()) == A)  # returns False
