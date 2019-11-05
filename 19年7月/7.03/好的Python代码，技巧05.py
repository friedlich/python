# 推导列表应该是我最喜欢的一种Pythonic方式，它的演变有很多手法，这几种都是非常常见的，多读几遍，背下来！

# 一个条件
print([x/2 for x in range(10) if x%2==0])
# 多个条件
print([x for x in range(30) if x%2==0 and x%6==0])
# 用if-else
print([x+1 if x>=5 else x*10 for x in range(10)])
# 嵌套推导列表
list_of_list = [[1,2,3],[4,5,6],[7,8]]
print([y for x in list_of_list for y in x])