# 编写爬虫逻辑
import scrapy,bs4
from  scrapy import log
from ..items import MeijuItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['zimuzu.tv']
    start_urls = ['http://www.zimuzu.tv/today']
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}  # 供登录模拟使用
    # 我们新建的MeijuSpider只继承了最普通的Spider，但是由于我们有可能需要做登录的操作，所以我们需要重载函数start_requests
    def start_requests(self):
        return [scrapy.FormRequest(
            url='http://www.zimuzu.tv/today',
            dont_filter=True,
            meta={'cookiejar': 1},
            callback=self.parse
        )]
    # 参数一个个来解析:
    # url:就是本次需要访问地址
    # dont_filter:是用于重复请求的，第一次请求发现需要登录操作，在登录操作完成后，要再一次访问这个url，如果不添加这个，会出现以下错误：
    # 2018-06-21 00:05:35 [scrapy.dupefilters] DEBUG: Filtered duplicate request: <GET http://www.zimuzu.tv/today> - no more duplicates will be shown (see DUPEFILTER_DEBUG to show all duplicates)
    # 2018-06-21 00:05:35 [scrapy.core.engine] INFO: Closing spider (finished)
    # 2018-06-21 00:05:35 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
    # meta={'cookiejar': 1}:这代表本次请求开启cookie
    # callback：设置本次访问成功后的回调函数

    # 首次回调
    def parse(self, response):
        log.msg(response.body.decode('utf-8'))
        # 判断有没有登录
        if "请登录" in response.body.decode('utf-8'):
            log.msg("need to login")
            log.msg("start login")
            return self.login(response)
        else:
            log.msg(response.body.decode('utf-8'))
            return self.getMovieList(response)
            # return self.login(response)
        # 首先我们拿到response后需要把它转换成utf-8的格式才能进行判断，如果有请登录，就进入登录流程，调用login函数
        def login(self,response):   
            fd = {'account':input('账号：'),#你的账号
                'password':input('密码：'),#你的密码
                'remember':'1',
                'url_back':'http%3A%2F%2Fwww.zimuzu.tv%2F'}
            return [scrapy.FormRequest(
                url='http://www.zimuzu.tv/User/Login/ajaxLogin',
                formdata=fd,
                meta={'cookiejar': response.meta['cookiejar']},
                callback=self.afterLogin
            )]
            # 就是做登录的请求，至于请求需要的字段，就是在浏览器抓取的，这次因为带有登录信息，所以就一次表单请求 
            # formdata:请求的表单数据集，回调函数是afterLogin
        def afterLogin(self,response):
            cookie = response.headers.getlist('Set-Cookie')

            # print('cookie:',cookie)
            url = 'http://www.zimuzu.tv/today'
            return [scrapy.FormRequest(
                url=url,
                dont_filter=True,
                meta={"cookiejar": True},
                callback=self.parse
            )]
            # 这个的日志我们可以看到打印出来的cookie信息：
            # cookie: [b’GINFO=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0; path=/; domain=.zimuzu.tv’, b’GKEY=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0; path=/; domain=.zimuzu.tv’, b’GINFO=uid%3D3548633%26nickname%3Dnickey0781%26group_id%3D1%26avatar_t%3Dhttp%3A%2F%2Ffiles.zmzjstu.com%2Fftp%2Favatar%2Ff_noavatar_t.gif%26main_group_id%3D0%26common_group_id%3D59; expires=Sun, 18-Jun-2028 15:40:04 GMT; Max-Age=315360000; path=/; domain=.zimuzu.tv’, b’GKEY=bb9df3e025695bfa45484ad26d7a3ac3; expires=Sun, 18-Jun-2028 15:40:04 GMT; Max-Age=315360000; path=/; domain=.zimuzu.tv; httponly’]
        # 接下来就可以用回第一个回调函数parse ，这次因为带上了cookie信息，所以是可以获得数据的，就会调用函数getMovieList
    def getMovieList(self, response):
        movies = response.xpath('//table[@class="d_r_t"][@day="06-17"]/tr')
        # movies = bs4.BeautifulSoup(movies.text).find_all(class_="list even")
        for m in movies:
            movieName = m.xpath('./td/a/text()').extract()
            # movieName = m.find('a').text.split('.')[0]
            print('move name size:',len(movieName))
            print('move name:',movieName)
            if (len(movieName) > 0):
                item = MovieItem()
                item['name'] = movieName
                yield item







