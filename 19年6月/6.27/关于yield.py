def a():
    for i in range(3):
        yield i
        yield i+10
aa = a()
for ii in aa:
    print(ii)

l = [1,2,3,4,5]
# next(l) TypeError: 'list' object is not an iterator
a = iter(l)
print(next(a))
print(next(a))

print(next(a))