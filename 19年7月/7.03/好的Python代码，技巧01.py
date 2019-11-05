# 快速构成一个字典序列
print(dict(zip('abcd',range(4))))
# 用类似3目运算输出
a=2
print('ok' if a==1 else 'ko')
# 直接return条件判断
def test(m):
    return 'a' if m==1 else 'b'
print(test(1))
# 推导列表生成字典
list1 = ((1,'a'),(2,'b'))
list2 = [(1,'a'),(2,'b')]
print(dict(list2))
print({x[0]:x[1] for x in list2})
print({x:y for x in range(4) for y in range(10,14)})

# 点评：
# Python因为简洁高效而出名，就是因为语法非常简单，而且内置了很多强大的数据结构：
# 比如我们可以大量用推导列表来生成很多简洁的代码
# 比如我们可以用if else组合，本来需要2-3行代码写的，一行搞定！

