# -*- coding: utf-8 -*-
import re
from scrapy import Spider, FormRequest, Request
from ..items import WeiboItem
import tushare as ts


class WeiboSpider(Spider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    search_url = 'https://weibo.cn/search/mblog'
    max_page = 5

    def start_requests(self):
        result = ts.get_hs300s()
        # result = ts.get_zz500s()
        keywords = result['code'].tolist()
        for keyword in keywords:
            sort = 'time'
            url = '{url}?keyword={keyword}&sort={sort}'.format(url=self.search_url, keyword=keyword, sort=sort)
            for page in range(self.max_page + 1):
                data = {
                    'mp': str(self.max_page),
                    'page': str(page)
                }
                yield FormRequest(url, callback=self.parse_index, formdata=data, meta={'keyword': keyword})

    def parse_index(self, response):
        # print(response.text)
        weibos = response.xpath('//div[@class="c" and contains(@id, "M_")]')
        # print(weibos)
        for weibo in weibos:
            is_forward = bool(weibo.xpath('.//span[@class="cmt"]').extract_first())  # //*[@id="M_I5uNddugI"]/div[1]/span[1]
            # // ename选择ename文档中的所有元素。
            # .// ename选择ename上下文节点或其下的所有元素。
            # print(is_forward)
            # XPath中的点称为“上下文项表达式”。如果在表达式的开头加上一个点，它将使其特定于上下文。换句话说，它将id = "Passwd"
            # 在您调用“通过XPath查找元素”方法的节点的上下文中搜索元素。
            # 将 * 在. // * [ @ id = 'Passwd']帮助匹配任何元素用id = 'Passwd'
            print(is_forward)
            if is_forward:
                detail_url = weibo.xpath('.//a[contains(., "原文评论[")]//@href').extract_first()  # 这个点还必须加上
            else:
                detail_url = weibo.xpath('.//a[contains(., "评论[")]//@href').extract_first()  # 感觉是前面weibo的原因
            # print(detail_url)
            yield Request(detail_url, callback=self.parse_detail, meta={'keyword': response.meta['keyword']})

    def parse_detail(self, response):
        id = re.search('comment\/(.*?)\?', response.url).group(1)
        url = response.url
        content = ''.join(response.xpath('//div[@id="M_"]//span[@class="ctt"]//text()').extract())
        print(id, url, content)
        comment_count = response.xpath('//span[@class="pms"]//text()').re_first('评论\[(.*?)\]')
        forward_count = response.xpath('//a[contains(., "转发[")]//text()').re_first('转发\[(.*?)\]')
        like_count = response.xpath('//a[contains(., "赞[")]//text()').re_first('赞\[(.*?)\]')
        print(comment_count, forward_count, like_count)
        posted_at = response.xpath('//div[@id="M_"]//span[@class="ct"]//text()').extract_first(default=None)
        user = response.xpath('//div[@id="M_"]/div[1]/a/text()').extract_first(default=None)
        print(posted_at, user)
        keyword = response.meta['keyword']
        weibo_item = WeiboItem()  # 引入WeiboItem并且实例化一下
        for field in weibo_item.fields:  # 遍历weibo_item中的所有fields，获取所有的字段名，field就是上面id,url这些
            try:
                weibo_item[field] = eval(field)  # eval可以动态的获取它的这些变量名，动态的进行赋值，不需要一个一个字段重写一遍
            except NameError:
                self.logger.debug('Field is Not Defined: ' + field)
        yield weibo_item




