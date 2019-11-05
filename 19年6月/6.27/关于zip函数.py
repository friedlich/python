# zip()采用一个或多个序列并将它们的元素编织在一起，就像map(None，…)对长度相等的序列一样。 
# 当最短的序列耗尽时，编织停止。
# zip()返回一个真正的Python列表，就像map()一样。

original = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
out1 = zip(*original)
print(out1)
print(type(out1))
list1 = []
for i in out1:
    list1.append(i)
    print(list1)
print(list1)

original = [('a', 1), ('b', 2), ('c', 3), ('d', 4),('e',)]
out2 = zip(*original)
list2 = []   # so, we need to show it in list
for i in out2:
    list2.append(i)
print(list2)

out = map(None, *[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', )])
print(out)
print(type(out))
# list3 = []
# for i in out:
#     list3.append(i)
# print(list3)

X=[1,2,3,4]
Y=['a','b','c','d']
XY=zip(X,Y)
print(XY)
x,y=zip(*XY)
print(x,y)
print(y)
