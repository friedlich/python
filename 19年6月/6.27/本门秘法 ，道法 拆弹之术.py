a=[['剑来1', '剑来2', '剑来3'], ['烽火戏诸侯', '老油条本尊', '暮鼓晨钟']]
b=['bookName','bookAuthor']
d= [dict(zip(b,z)) for z in zip(*tuple(a))]
print(*tuple(a))
print(d)

print(*[1,2,3])
print([1,2,3])
print((1,2,3))
print(*(1,2,3))

a=[['剑来1', '剑来2', '剑来3'], ['烽火戏诸侯', '老油条本尊', '暮鼓晨钟']] 
# 这里的a是一个列表，里面装的是两个列表，和b列表里面的两个字符串一一对应打包起来
b=['bookName','bookAuthor']
c=['剑来1', '剑来2', '剑来3']

d= [dict(zip(b,z)) for z in zip(*a)]
print(zip(b,a)) # zip应该是一一对应打包的意思
print(*a) 
# 这里的最外层是两个量了，和b已经不是一一对应了，是一对二的形式，所以要嵌套字典，里面装的是字符串，和b对应起来
print(dict(zip(b,a)))
print(d)
print(dict(zip(b,c)))