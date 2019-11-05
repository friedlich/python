import re

content = '''Hello 123456 World_This
is a Regex Demo'''
result = re.match('^He.*?(\d+).*?Demo$',content,re.S)
print(result)
print(result.group(1))

