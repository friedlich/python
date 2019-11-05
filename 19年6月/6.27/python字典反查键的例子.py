movies = {'妖猫传':['黄轩','柒谷将太'],'无问西东':['章子怡','王力宏','祖峰'],'超时空同居':['雷佳音','佟丽娅']}
actor = input('你想查询哪个演员')
for k,v in movies.items():
    # print(k,v)
    if actor in v:
        print(actor + '出演了电影：' + k)