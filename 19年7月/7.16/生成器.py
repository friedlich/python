# 生成器会生成一系列的值用于迭代，这样看它又是一种可迭代对象。它是在for循环的过程中不断计算出下一个元素，
# 并在适当的条件结束for循环。我们定义一个能逐个“yield”值的函数，然后用一个for循环来迭代它。
def squares(n):
    i=1
    while(i<=n):
       yield i**2
       i+=1
a = squares(5)
print(next(squares(5))) 
print(next(squares(5))) # 这两句其实是一样的，相当于是分两次重新next了一下squares()生成器,所以都只next了一下，打印出1
print(next(a))
print(next(a)) # 这就很神奇，a应该是一个迭代器了，因为可以用next()，不过还是会很奇怪，懂了
print(a)
for i in squares(5):
   print(i)