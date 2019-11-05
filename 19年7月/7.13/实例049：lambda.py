# 题目 使用lambda来创建匿名函数。
# 程序分析 无
Max=lambda x,y:x*(x>=y)+y*(y>x)
Min=lambda x,y:x*(x<=y)+y*(y<x)
Sum_x=lambda x,y:x*(x<y)+y*(x<y)
Sum_y=lambda x,y:x*(y<x)+y*(y<x)

a=int(input('1:'))
b=int(input('2:'))

print(Max(a,b))
print(Min(a,b))
print(Sum_x(a,b))
print(Sum_y(a,b))

