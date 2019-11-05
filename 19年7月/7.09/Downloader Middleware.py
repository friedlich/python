# 举例：我们来定义一个随机产生User-Agent的Downloader Middleware，这样我们就能随
# 机地给每个Requests的headers加上User-Agent了

# 实现功能：给每个Requests的请求头中添加随机User-Agent，代码看不懂没有关系，只是做个示例演示⼀下可以这么做来应对反爬

## settings.py中要修改的配置
USER_AGETN_LIST = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36']
DOWNLOADER_MIDDLEWARES = {
'Douban.middlewares.DoubanDownloaderMiddleware': 543,
'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
'Douban.middlewares.RandomUserAgentMiddleware': 1,
}

## middlewares.py中要书写的代码
import random
class RandomUserAgentMiddleware(object):
    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        self.user_agent_list = crawler.settings.get('USER_AGETN_LIST', [])

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        user_agent = random.choice(self.user_agent_list)
        request.headers.setdefault('User-Agent', user_agent)

# 当然，这种⽅式在实际编程中并不是⼀个好的选择，因为这需要我们⾃⼰维护⼀个USER_AGENT_LIST，⽽且这个USER_AGENT_LIST还是写死了
# 的，⼀旦改变了其中的值，要使其⽣效，⼜得重新运⾏Scrapy项⽬。

### 
# ⼀般我们会⽤到⼀个第三⽅库，叫做fake-useragent，来帮助我们随机⽣成User-Agent，具体安装和⽤法如下：
# https://github.com/hellysmile/fake-userag
# 实现功能：对于随机⽣成User-Agent的⼀个更好地选择

## settings.py中要修改的配置
DOWNLOADER_MIDDLEWARES = {
'Douban.middlewares.DoubanDownloaderMiddleware': 543,
'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
'Douban.middlewares.RandomUserAgentMiddleware': 1,
}

## middlewares.py中要书写的代码
# from fake_useragent import UserAgent
class RandomUserAgentMiddleware(object):
    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()
        # self.ua = UserAgent()
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)
    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', self.ua.random)




