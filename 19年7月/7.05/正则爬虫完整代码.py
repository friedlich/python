# 以上，就完成了所有的代码了，所有的代码整合一下，就是下面的完整代码：

# 实现功能：利用正则表达式提取电影名称/上映时间/上映地点/电影分类/电影评分
import re
import requests
url_list = []
movie_informations = []
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
for i in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(25*i) + '&filter='
    url_list.append(url)
for url in url_list:
    response = requests.get(url, headers=headers)
    content = response.text.replace(' ', '').replace('\n', '')
    all_tags = re.findall('.*grid_view.*?(<li>.*</li>)', content, flags=re.S)[0]
    movie_tags = re.findall('<li>.*?</li>', all_tags)
    # print(len(movie_tags))
    for movie_tag in movie_tags:
        movie_name = re.findall('.*?class="title">(.*?)<', movie_tag)[0]
        other = re.findall('.*?class="bd".*?<br>(.*?)</p>.*', movie_tag)[0]
        release_date = int(re.findall('\d+', other)[0])
        release_place = re.findall('.*?/(.*?)/', other)[0].replace('&nbsp;', '')
        release_category = re.findall('.*/(.*)', other)[0].replace('&nbsp;', '')
        movie_rate = float(re.findall('.*?rating_num.*?>(.*?)<.*?', movie_tag)[0])
        movie_informations.append((movie_name, release_date, release_place, release_category, movie_rate))
for index, movie_information in enumerate(movie_informations):
    movie_name, release_date, release_place, release_category, movie_rate = movie_information
    # 这一行为序列的解包
    print(index+1, movie_name, release_date, release_place, release_category, movie_rate)

# 好啦，今天的分享到这里就结束了，如果能够掌握这个例子的应用，那么你掌握的正则基本能够应对你的日常所需了。
# 对于我们学到的知识，应该多实践，尤其是编程，一定要多写代码，大家加油。