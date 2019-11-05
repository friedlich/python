import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
print(result)
print(result.group())
print(result.span())

result1 = re.match('^Hello.*Demo$',content)
print(result)
print(result.group())
print(result.span())

content = 'Hello 1234567 World_This is a Regex Demo'
result2 = re.match('^Hello\s(\d+)\sWorld.*Demo$',content)
print(result2)
print(result2.group())
print(result2.group(1))
print(result2.span())