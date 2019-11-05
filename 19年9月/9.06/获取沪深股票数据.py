import tushare as ts

result = ts.get_hs300s()
# print(result)
print(type(result))
print(result['name'].tolist())
print(result['code'].tolist())