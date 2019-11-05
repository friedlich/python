# 一、在for循环中直接更改列表中元素的值不会起作用：
# 如：	
l = list(range(10)[::2])
print(l)
for n in l:
    n = 0
print(l)
# 运行结果：
# [0, 2, 4, 6, 8]
# [0, 2, 4, 6, 8]
# l中的元素并没有被修改

# 二、在for循环中更改list值的方法：
# 1.使用range

l = list(range(10)[::2])
print(l)
for i in range(len(l)):
    l[i] = 0
print(l)
# 运行结果：
# [0, 2, 4, 6, 8]
# [0, 0, 0, 0, 0]

# 2.使用enumerate	
l = list(range(10)[::2])
print(l)
for index,value in enumerate(l): 
    l[index] = 0 
print(l)
# 运行结果：
# [0, 2, 4, 6, 8]
# [0, 0, 0, 0, 0]