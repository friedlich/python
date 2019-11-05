movie = '''
                            1994 / 美国 / 犯罪 剧情
                        '''
# 我们实际能获取到的数据是这样的，现在我们要去掉首尾多余的空格，可以这么做
movie = movie.strip()
print(movie)
# strip()表示去除首尾的空格，这个对字符串的处理用得非常多
# 得到的结果就是1994 / 美国 / 犯罪 剧情


# 经过strip()处理之后，可以看到得到得结果中仍然还是有空格，这个就可以用replace来替
# 换掉空格。
movie1 = movie.replace(' ','')
# 这一行表示将字符串中的空格替换掉，replace第一个参数表示要替换的字符串，第二个参数表示要用什么来替换。
# 得到的结果就是1994/美国/犯罪剧情
print(movie1)
import re
movie = re.sub('\s', '', movie)
print(movie)


# 经过replace()处理之后，其实得到的数据已经可以了，但是，如果我们想分别提取出上映年份/上映地点/电影分类呢。
# 这个时候就用到我们之前用过的split了。
movie = movie.split('/')
# 这一行表示将字符串通过/进行分割，得到的是一个列表
# 得到的结果是['1994', '美国', '犯罪剧情']
print(movie)


origin_url = 'https://www.zhihu.com'
url_list = ['/question/36539555/answer/595275293','/question/308663552/answer/577063117','https://www.zhihu.com/special/20743868']
for i in range(len(url_list)):
    if not url_list[i].startswith('http'):  
        url_list[i] = origin_url + url_list[i]
# 这一行表示如果url_list[i]不是以http开头的话，那么就执行if内部的语句
print(url_list)

url_list = ['https://pic2.zhimg.com/50/v2‐5502c54842dceeb2e8901e884407a7fd_fhd.jpg',
'https://www.zhihu.com/special/20743868']
for url in url_list:
    if url.endswith('jpg'):
        url_list.remove(url)
print(url_list)


# 最后，我们再来谈一个join方法，这个方法是用来拼接一个序列（列表/元组等）的值的，将一个序列转换一个字符串。
tag = ['文学','短篇小说','小说','先锋文学']
tag = '-'.join(tag)
print(tag)


# 实现功能：将列表中相同的元素去重，统计书籍词汇量
content = ['Whatever','is','worth','doing','is','worth','doing','well']
new_content = set(content)
# 这一步是将列表转换成集合，就去重成功了，因为集合内的元素是不能重复的，但它是无序的
new_content = list(new_content)
# 这一步是将上一步得到的集合转换成一个列表，这样就得到了最终结果列表了
print(new_content)
# 得到的结果是['worth', 'Whatever', 'is', 'doing', 'well']



