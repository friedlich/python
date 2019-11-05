def dummy():
    i=0
    i+=1
    print(i) 
    i+=1
def dummy2():
    global n
    n+=1
    print(n)
    n+=1
i=0
n=0
print('函数内部的同名变量')
for j in range(3):
    print(i)
    dummy()
    i+=5
print('global声明同名变量')
for k in range(3):
    print(n)
    dummy2()
    n+=10

