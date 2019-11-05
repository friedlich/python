a=[['剑来1', '剑来2', '剑来3'], ['烽火戏诸侯', '老油条本尊', '暮鼓晨钟']]
b=['bookName','bookAuthor']
print(len(b))
print(dict(zip(b,a)))
c=[
{'bookName':'剑来1','bookAuthor':'烽火戏诸侯'},
{'bookName':'剑来2','bookAuthor':'老油条本尊'},
{'bookName':'剑来3','bookAuthor':'暮鼓晨钟'},
]
print('\n')

d= [{b[0]:x,b[1]:y} for x,y in zip(a[0],a[1])]
print(d)
print('\n')

lists=[]
for i in range(len(a[0])): #3:0,1,2
    dic={}
    for j in range(len(b)): #2:0,1
        dic[b[j]]=a[j][i]
        print(dic)
    lists.append(dic)
    print(lists)
print(lists)
print('\n')


