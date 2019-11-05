import json
# 引入json模块
a = [1,2,3,4]
# 创建一个列表a。
b = json.dumps(a)
# 使用dumps()函数，将列表a转换为json格式的字符串，赋值给b。
print(b)
# 打印b。
print(type(b))
# 打印b的数据类型。
c = json.loads(b)
# 使用loads()函数，将json格式的字符串b转为列表，赋值给c。
print(c)
# 打印c。
print(type(c)) 
# 打印c的数据类型。

with open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\6.15\result.json','w') as f:
    json.dump(a,f)

with open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\6.15\result1.json','w') as f:
    json.dump(b,f)

# with open(r'C:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\6.15\result.json1','w') as f:
#     json.load(b)

# json.dumps 将 Python 对象编码成 JSON 数据
# json.dump 将 JSON 数据通过特殊的形式转换为只有 Python 认识的字符串并写入文件
# json.loads 将已编码的 JSON 数据解码为 Python 对象
# json.load 将一个包含 JSON 格式数据的可读文件解码为一个 Python 对象并写入文件