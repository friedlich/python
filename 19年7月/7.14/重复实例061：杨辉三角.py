def generate(num):
    r = [[1]]
    for i in range(1,num):
        r.append(list(map(lambda x,y:x+y, [0]+r[-1],r[-1]+[0])))
    return r

a = generate(6)
for i in a:
    print(i)

# 大概输出过程就是这样：
[[1]]
[0,1],[1,0]
[[1],[1,1]]
[0,1,1],[1,1,0]
[1,2,1]
[[1],[1,1],[1,2,1]]