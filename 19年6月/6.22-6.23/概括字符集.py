import re
target = 'life is short \n i love python'
print(re.findall('\s', target))
print(re.findall('\S', target))

target = 'i love python_'
print(re.findall('\w', target))
print(re.findall('\W', target))

target = '点赞数：12'
print(re.findall('\d', target))
print(re.findall('\D', target))
