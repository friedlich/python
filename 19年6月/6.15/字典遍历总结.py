#字典遍历总结
dict1 = {'name':'jim','age':25,'score':96}

#遍历键
for k in dict1.keys():
    print(k)
print('\n')
#遍历值
for v in dict1.values():
    print(v)
print('\n')
#遍历键和值
for k,v in dict1.items():
    print(k,v)
print('\n')
#************可耻的分割线*****************
 
#默认等价于遍历键
for k in dict1:
    print(k)
print('\n')
#常用套路：遍历键取值
for k in dict1:
    print(dict1[k])