# 题目 打印出杨辉三角形前十行。
# 程序分析 无。
def generate(numRows):
    r = [[1]]
    print(r[-1])
    print([0]+[1])
    for i in range(1,numRows):
        r.append(list(map(lambda x,y:x+y, [0]+r[-1],r[-1]+[0])))
        print(r)
    return r[:numRows]
a=generate(5)
print(a)
for i in a:
    print(i)

b = [1,2,3,4,5]
c = b[:5]
d = b[2]
e = b[2:4]
print(c)
print(d)
print(e)
