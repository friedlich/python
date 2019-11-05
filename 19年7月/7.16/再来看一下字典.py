dict = {}
dict['one'] = 'This is one'
dict[2] = 'This is two'
tinydict = {'name':'john','code':5762,'dept':'sales'} 
print(dict['one']) #输出键为'one'的值
print(dict[2]) #输出键为2的值
print(tinydict) #输出完整的字典
print(tinydict.keys()) #输出所有键
print(tinydict.values()) #输出所有值
for k in tinydict.keys():
    print(k)
for v in tinydict.values():
    print(v)
for k ,v in tinydict.items():
    print(k,v)