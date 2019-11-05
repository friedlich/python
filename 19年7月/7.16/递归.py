# 在调用一个函数的过程中，直接或间接地调用了函数本身这个就叫递归。但为了避免出现死循环，必须要有一个结束条件，举个例子：
def facto(n):
    if n==1: return 1
    return n*facto(n-1)
print(facto(5))