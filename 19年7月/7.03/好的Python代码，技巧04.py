# 有的时候我们会遇到复杂的数据结构，比如列表里面套列表，层层嵌套，非常麻烦。有几种方法可以碾平:
# 1).第一种传统方法
# Isinstance的用法是用来判断一个量是否是相应的类型，接受的参数一个是对象加一种类型。示范代码如下：
a = 1
print(isinstance(a,int))
print(isinstance(a,float))

s = [1,[2,[3,4]]]
res = []
def fun(s):
    for i in s:
        if isinstance(i,list):
            fun(i)
        else:
            res.append(i)
fun(s)
print(res)
# 点评：这里面就是用递归来解决的，思路非常简单清晰，但是递归一定要有出口，设计的时候要注意。

# 2).下面两种都是高手的写法
flat = lambda L: sum(map(flat,L),[]) if isinstance(L,list) else[L] # 这里if之前的L是列表
# 这他妈是真理解不了
# flat = lambda L: sum(map(flat,L) if isinstance(L,list) else[L] ,[]) 
# flat = lambda L: map(flat,L) if isinstance(L,list) else sum(L,[])
# L = [1,[2,[3,4]]]
# def flat(L):
#     if isinstance(L,list):
#         lambda L: sum(map(flat,L),[])
#     else:
#         [L]
print(flat(s))
print(sum((2, 3, 4), 1) )
l = [[1],[2],[3],[4]]
flat = lambda L: sum(map(flat,L),[]) if isinstance(L,list) else[L]
print(flat(l))
print(flat(s))
flat = lambda L: sum(L,[])
print(flat(l))

a = [1,2,[3,4],[[5,6],[7,8]]]
# flatten = lambda x: [y for l in x for y in flatten(l)] if type(isinstance(x,list)) else [x]
# print(flatten(a))
# 点评：这两招看上去非常简单，实际上理解起来很复杂，把很多技巧结合在一行里面，反正第二种我还能接受，
# 第三种口味太重了，看的有点晕！
print(sum([[1],[2]],[]))

a1 = [[1],[2],[3],[4]]
a2 = [[3]]
way = lambda x: sum(x,[])
print(way(a1))
print(way(a2))

add=lambda x, y: x+y
print(add(1,2))
# 这个理解真是有些烧脑