scores = dict()
print(scores)
find_all = []
# scores[int(num)-1] = star
scores[0] = '9.6'
scores[1] = '9.6'
scores[2] = '9.4'
scores[3] = '9.4'
scores[4] = '9.5'
print(scores)
for k in scores.keys():
    print(scores[k])
# print(scores.items)
for k,v in scores.items():
    print(k,v)
order = sorted(scores.values(),key = lambda x:x[-1],reverse = True)
print(order)
order = sorted(scores.items(),key = lambda x:x[-1],reverse = True)
print(order)
# order = sorted(scores.keys(),key = lambda x:x[-1],reverse = True)
# print(order) # TypeError: 'int' object is not subscriptable
print(dict(order))
for i in dict((order)):
    print(i)