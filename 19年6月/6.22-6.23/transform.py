from urllib.request import quote,unquote
import re

params = input('请复制params到这里：') # 这里是解码
de = unquote(params,encoding="utf-8")
print(de)
en = quote(params,encoding="utf-8")
e = quote(params,encoding="gbk") # 这里是编码
print(en)
print(e)

result = re.split('&',de)
print(result)
result_dic = {}
for item in result:
    item_list = re.split('=',item)
    print(item_list)
    key = item_list[0]
    try:
        value = item_list[1]
    except IndexError:
        value = ''
    result_dic[key] = value
print(result_dic)

list_dict = [result_dic]
print(list_dict)
# for k,v in result_dic.items():
#     print(k,v)
        
# %E5%91%A8%E6%9D%B0%E4%BC%A6%27

