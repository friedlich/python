info = [0,1,2,3,4,5,6,7,8,9]

a = [i+1 for i in range(10)]
print(a)

b = ['{}'.format(i+1) for i in info]
print(b)

c = ['{},{}'.format(i,i+1) for i in info]
print(c)
