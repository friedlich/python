# -*- coding: utf-8 -*-
import json

from scrapy import Request, Spider
from ..items import UserItem


class ZhihuSpider(Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    start_user = 'excited-vczh'

    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'

    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    next_page = 'https://www.zhihu.com/members/excited-vczh/followees?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=40'
    # 终于被我给发现了，原来是这个网站失效了

    def start_requests(self):
        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), self.parse_user)
        yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20), self.parse_follows)
        yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, limit=20, offset=0), self.parse_followers)

    def parse_user(self, response):
        result = json.loads(response.text)
        item = UserItem()
        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        yield Request(
            self.follows_url.format(user=result.get('url_token'), include=self.follows_query, offset=0, limit=20),
            self.parse_follows)

        yield Request(
            self.followers_url.format(user=result.get('url_token'), include=self.followers_query, limit=20, offset=0),
            self.parse_followers)

    def parse_follows(self, response):
        results = json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)

        # if 'paging' in results.keys() and results.get('paging').get('is_end') == 'false':
        # 这个没作用无反应，从网页里面来看它也不是一个字符串，没有引号，而是一个fsale布尔值
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            # yield Request(next_page,
            #               self.parse_follows)
            yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=20, limit=20), self.parse_follows)
            print('可以找到下一页')

        # if 'paging' in results.keys():
        #     next_page = results['paging']['next']
        #     yield Request(next_page, self.parse_follows)

    def parse_followers(self, response):
        results = json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),
                              self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(self.followers_url.format(user=self.start_user, include=self.followers_query, offset=20, limit=20), self.parse_followers)


#  DEBUG: Crawled (404) <GET https://www.zhihu.com/members/excited-vczh/followees?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%2Cfollow
# er_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=60> (referer: https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=dat
# a[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics&offset=40&limit=20)

#  DEBUG: Crawled (404) <GET https://www.zhihu.com/members/excited-vczh/followees?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%2Cfollow
# er_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=20> (referer: https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=dat
# a[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics&offset=0&limit=20)

# DEBUG: Crawled (200) <GET https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data[*].answer_count,articles_count,gender,follower_co
# unt,is_followed,is_following,badge[?(type=best_answerer)].topics&offset=0&limit=20> (referer: None)

# next_page = 'https://www.zhihu.com/members/excited-vczh/followees?include=data%5B%2A%5D.answer_count%2Carticles_count%2Cgender%2Cfollow
# er_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=40'

# HTTP status code is not handled or not allowed 不处理或不允许HTTP状态代码

# 404错误是客户端在浏览网页时，服务器无法正常提供信息，或是服务器无法回应，且不知道原因所返回的页面。
#
# 404错误信息大部分是网站的问题，通常在网站目标页面被更改或移除后，就会显示404错误页面。有时候客户端输入页面地址错误后，也会显示404错误页面。
#
# 在http请求3位的返回码中，4开头的代表客户错误，5开头代表服务器端错误。

# HTTP 404 错误意味着链接指向的网页不存在，即原始网页的URL失效，这种情况经常会发生，很难避免，比如说：网页URL生成规则改变、网页文件更名或移动位置、导入链接拼写错误等，导致原来的URL地址无法访问；
#
# 当Web 服务器接到类似请求时，会返回一个404 状态码，告诉浏览器要请求的资源并不存在。导致这个错误的原因一般来说，有三种：
#
# 1、无法在所请求的端口上访问Web站点。
#
# 2、Web服务扩展锁定策略阻止本请求。


