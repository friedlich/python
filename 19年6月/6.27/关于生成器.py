a=[['剑来1', '剑来2', '剑来3'], ['烽火戏诸侯', '老油条本尊', '暮鼓晨钟']]
A = (pow(i,2) for i in range(2))
b = [pow(i,2) for i in range(2)]
c = (i+2 for i in range(2))
d1 = [dict(zip(b,i))for i in zip(*a)]
d4 = [dict(zip(b,i))for i in zip(A)]
d2 = [dict(zip(b,i)for i in zip(*a))]
d3 = [dict(zip(c,i))for i in zip(*a)]
print(zip(*a))
print(next(zip(*a)))
print(next(zip(*a)))
print(d1)
print(d2)
print(d3)
print(d4)

f = (i for i in range(10))
print(type(f))
print(f)
print(next(f))
print(next(f))