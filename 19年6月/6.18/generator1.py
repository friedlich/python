# 列表生成式
lis = [x*x for x in range(10)]
print(lis)

# 生成器
generator_ex = (x*x for x in range(10))
# print(generator_ex)
print(next(generator_ex))
print(next(generator_ex))

# for i in generator_ex:
#     print(i)

def fib(max):
    n,a,b=0,0,1
    while n<max:
        a,b=b,a+b
        n=n+1
    return a,b
b = fib(10)
# print(b.__next__())   会报错：'tuple' object has no attribute '__next__'

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield a,b
        # 生成器是一个特殊的程序，可以被用作控制循环的迭代行为，python中生成器是迭代器的一种，
        # 使用yield返回值函数，每次调用yield会暂停，而可以使用next()函数和send()函数恢复生成器。
        a,b=b,a+b
        n=n+1
    return 'done'
a = fib(10) # 因为yield的存在，现在的 a 是一个生成器；带有yield的函数不再是一个普通的函数，而是一个
# 生成器generator，可用于迭代
print(fib(10))

print(a.__next__())
# print(a.__next__())
print(a.send(6)) # 这个6没有赋值进去的话，和next是同样的效果
print(a.__next__())
print("可以顺便干其他事情")
print(a.__next__())
print(a.__next__())
# 在上面fib的例子，我们在循环过程中不断调用 yield ，就会不断中断。当然要给
# 循环设置一个条件来退出循环，不然就会产生一个无限数列出来。


