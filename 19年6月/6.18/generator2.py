def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        # 生成器是一个特殊的程序，可以被用作控制循环的迭代行为，python中生成器是迭代器的一种，使用yield返回值函数，
        # 每次调用yield会暂停，而可以使用next()函数和send()函数恢复生成器。我们在循环过程中不断调用 yield ，就会
        # 不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
        a,b=b,a+b
        n=n+1
    return 'done'
# for i in fib(6):
#     print(i)
g = fib(6)
print(g)
while True:
    try:
        x = next(g)
        print('generator: ',x)
    except StopIteration as e:
        print('生成器返回值：'+e.value)
        break