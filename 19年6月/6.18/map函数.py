def add(x,y,z):
    return x,y,z

list1 = [1,2,3]
list2 = [1,2,3,4]
list3 = [1,2,3,4,5]
res = list(map(add, list1, list2, list3))
print(res)

a=(1,2,3,4,5)
b=[1,2,3,4,5]
c="lh"
 
la=tuple(map(str,a))
lb=list(map(str,b))
lc=set(map(str,c))

print(la)
print(lb)
print(lc)

# map函数的原型是map(function, iterable, …)，它的返回结果是一个列表。
# 参数function传的是一个函数名，可以是python内置的，也可以是自定义的。 参数iterable传的是一个可以迭代的对象，
# 例如列表，元组，字符串这样的。
# 这个函数的意思就是将function应用于iterable的每一个元素，结果以列表的形式返回。iterable后面还有省略号，
# 意思可以传很多个iterable，如果有额外的iterable参数，并行的从这些参数中取元素，并调用function

a=list(map(str,'python'))
print(a)

def add(x,y):
    return x+y
list1=[1,2,3]
list2=[4,5,6]
a=list(map(add,list1,list2))
print(a)

def add(x,y):
    return x,y
print(add(2,3))
list1 = [1,2,3]
list2 = [1,2,3,4]
a = list(map(add, list1, list2))
print(a)