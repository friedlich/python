import re

content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result = re.match('Hello.*?(\d+).*?Demo',content)
print(result)
result = re.search('Hello.*?(\d+).*?Demo',content)
print(result)
print(result.group(1))