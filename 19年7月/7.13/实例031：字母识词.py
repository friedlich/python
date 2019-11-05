# 题目 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析 这里用字典的形式直接将对照关系存好。
weekT = {'u':'tuesday',
        'h':'thursday'}
weekS = {'a':'saturday',
        'u':'sunday'}
week = {'m':'monday',
        't': weekT,
        'w':'wensday',
        'f':'friday',
        's': weekS}
a = week[str(input('请输入星期几的第一个字符：')).lower()]
if a==weekT or a==weekS:
    print(a[input('请输入星期几的第二个字符：').lower()])
else:
    print(a)

    