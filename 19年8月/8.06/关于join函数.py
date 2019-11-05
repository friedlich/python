# 1、join函数

# 用法：用于连接字符串数组。将字符串、元组、列表中的元素以指定的字符（即分隔符）连接生成一个新的字符串

# 语法：'sep'.join(seq)

# 参数说明：sep：分隔符，可以为空；seq：要连接的元素序列、字符串、元组、字典等

# 返回值：返回一个以分隔符sep连接各个元素后生成的新字符串

# 2、os.path.join函数

# 用法：将多个路径组合后返回

# 语法：os.path.join(path1[,path2[,path3[,...[,pathN]]]])

# 返回值：将多个路径组合后返回

# 注意：第一个绝对路径之前的参数将会被忽略


# 对字符串进行操作
seq1 = "my name is vampire techking"
print(':'.join(seq1))
# 对元组进行操作
seq2 = ('my','name','is','vampire','techking')
print(':'.join(seq2))
# 对序列（列表）进行操作
seq3 = ['my','name','is','vampire','techking']
print(':'.join(seq3))
# 对字典进行操作
seq4 = {'my','name','is','vampire','techking'}
print(':'.join(seq4))
# 合并路径
import os
print(os.path.join('/my/','name/is/','vampire_techking'))
print(os.path.join('/my/','name/is/','/vampire_techking'))
print(os.path.join('/my/','/name/is/','vampire_techking'))

# 应用（九九乘法表）：
print('\n'.join([' '.join(['%s*%s=%-2s'%(y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))