# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import json
import logging
import requests
from requests.exceptions import ConnectionError
from scrapy.exceptions import IgnoreRequest


class CookiesMiddleware():

    def __init__(self, cookies_pool_url):
        self.logger = logging.getLogger(__name__)  # 可以直接获取一个logger，返回一个名称为name的Logger实例
        self.cookies_pool_url = cookies_pool_url

    def _get_random_cookies(self):
        try:
            response = requests.get(self.cookies_pool_url)
            if response.status_code == 200:
                return json.loads(response.text)
        except ConnectionError:
            return None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            cookies_pool_url=crawler.settings.get('COOKIES_POOL_URL')
        )

    def process_request(self, request, spider):
        # cookies = self._get_random_cookies()
        cookies = {
            'SUB': '_2A25wdX7VDeRhGeBM71IR9y3FzDyIHXVTlgKdrDV6PUJbkdANLVr5kW1NRMmDYkW1q6BLRigutHsy-qX118o25YV4',
            'SUHB': '0z1AsFny3NYZ36',
        }
        # 又发现了一个事情，就是我退出登录后，我的cookies会失效，就是302状态码，原来我的异常处理里面是有这个点的呀
        # 302Found，原始描述短语为MovedTemporarily，是HTTP协议中的一个状态码(StatusCode)。可以简单的理解为该资源原本确实存在，
        # 但已经被临时改变了位置；换而言之，就是请求的资源暂时驻留在不同的URI下，故而除非特别指定了缓存头部指示，该状态码不可缓存
        # 301转向(或叫301重定向，301跳转)是当用户或搜索引擎向网站服务器发出浏览请求时，服务器返回的HTTP数据流中头信息(header)
        # 中的状态码的一种，表示本网页永久性转移到另一个地址。301重定向主要是将需要转移的网址重定向另一个新的网址上，并且是永久性转移。
        print(type(cookies))
        # cookies = requests.utils.cookiejar_from_dict(cookies)
        # print(type(cookies))
        if cookies:
            request.cookies = cookies  # 这里必须是request
            self.logger.debug('Using Cookies ' + json.dumps(cookies))
        else:
            self.logger.debug('No Valid Cookies')

    def process_response(self, request, response, spider):
        if response.status in [300, 301, 302, 303]:
            try:
                redirect_url = response.headers['location']
                if 'passport' in redirect_url or 'login.sina' in redirect_url:  # Cookie失效
                    self.logger.warning('Updating Cookies')
                elif 'weibo.cn/security' in redirect_url:
                    self.logger.warning('Now Cookies' + json.dumps(request.cookies))
                    self.logger.warning('One Account is locked!')
                request.cookies = self._get_random_cookies()
                self.logger.debug('Using Cookies' + json.dumps(request.cookies))
                return request
            except Exception:
                raise IgnoreRequest
        elif response.status in [414]:
            return request
        else:
            return response

