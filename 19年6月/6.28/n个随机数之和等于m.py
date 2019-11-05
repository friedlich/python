import random

def sum(m,n):
    b=m
    z=0
    total=[]
    while True:
        y=m-n+1
        x=random.randint(0,y)
        n-=1
        m=m-x-n+1
        total.append(x)
        print(total)
        z=z+x
        if n==1:
            break
    a=b-z
    total.append(a)
    print(total)

sum(100,5)


import random
def f(m,n):
    l = [ 1 for i in range(n)]
    for _ in range(m-n):
        k = random.randint(0,n-1)
        l[k]+=1
    return l

print(f(10,6))


# import numpy as np
# m=100
# n=10
# xx-=-np.random.randint(0,m.n-1)
# xx-=-np.append(xx,m)
# xx-=-np.sort(xx)
# xx-=-np.append(xx[1:]-xx[:-1],xx[0])

    