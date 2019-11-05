###
# 函数有了yield之后，函数名+（）就变成了生成器
# return在生成器中代表生成器的中止，直接报错
# next的作用是唤醒并继续执行
# send的作用是唤醒并继续执行，发送一个信息到生成器内部
'''生成器'''
def create_counter(n):
    print('create_counter')
    while True:
        yield n # 到这里生成器会停住，等待下一个next(gen)来激活，这里的n居然是会被打印出来的
        # a = yield
        print('increment n')
        # print(a)
        n += 1
        # print(n)

gen = create_counter(2)
# gen.__next__() # 这里其实也是进行了一次
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
# print(gen.send(5))
# print(gen.send(5))
# print(gen.send(9))



# AttributeError: 'generator' object has no attribute 'next'

# Process finished with exit code 0


# 1 >>> # 列表解析生成列表
# 2 >>> [ x ** 3 for x in range(5)]
# 3 [0, 1, 8, 27, 64]
# 4 >>>
# 5 >>> # 生成器表达式
# 6 >>> (x ** 3 for x in range(5))
# 7 <generator object <genexpr> at 0x000000000315F678>
# 8 >>> # 两者之间转换
# 9 >>> list(x ** 3 for x in range(5))
# 10 [0, 1, 8, 27, 64]