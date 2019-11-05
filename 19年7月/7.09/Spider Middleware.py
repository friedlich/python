# 举例：Scrapy源码中已经提供了一些Spider Middleware，我们可以按照Scrapy提供的例子来书写我们自己的Spider Middleware，
# 这里，我们只分析下Scrapy源码中的一个Spider Middleware，叫做HttpErrorMiddleware

# 实现功能：⾃定义对Response的处理，针对不同的Response状态码对Response进⾏过滤

# 这部分源码在scrapy.spidermiddlewares.httperror中
class HttpErrorMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        # 这个⽅法是必须要实现的，Middleware的manager会调⽤这个⽅法
        return cls(crawler.settings)

    def __init__(self, settings):
        self.handle_httpstatus_all = settings.getbool('HTTPERROR_ALLOW_ALL')
        self.handle_httpstatus_list = settings.getlist('HTTPERROR_ALLOWED_CODES')

    def process_spider_input(self, response, spider):
        # 真正的处理逻辑，判断是否将Response发送给Spider
        if 200 <= response.status < 300: # common case
            # 如果状态码在200-300之间就直接将Response发送给Spider
            return
        meta = response.meta
        if 'handle_httpstatus_all' in meta:
            # handle_httpstatus_all是我们可以⾃定义的⼀个配置，表示的内容为“是否选择⾃⼰处理所有状态码”，如果为True，
            # 那么⽆论Response的状态码是多少，都会返回给Spider
            return
        if 'handle_httpstatus_list' in meta:
            # handle_httpstatus_list也是我们可以⾃定义的⼀个配置，表示的内容为“允许处理的状态码”，
            # 假设handle_httpstatus_list = [404, 403, 301]，那么状态码在这个列表⾥的Response都
            # 不会过滤掉，会返回给Spider
            allowed_statuses = meta['handle_httpstatus_list']
        elif self.handle_httpstatus_list:
            # 如果我们没有⾃定义handle_httpstatus_list，那么会获取Scrapy配置的默认值，为True
            return
        else:
            allowed_statuses = getattr(spider, 'handle_httpstatus_list', self.handle_httpstatus_list)
        if response.status in allowed_statuses:
            return
        raise HttpError(response, 'Ignoring non-200 response')
        # 如果⾃定义的Response的过滤规则，那么就直接抛出⼀个异常，会被下⾯的process_spider_exception接收到，从⽽进⾏处理

    def process_spider_exception(self, response, exception, spider):
        # 处理抛出的异常
        if isinstance(exception, HttpError):
            spider.crawler.stats.inc_value('httperror/response_ignored_count')
            spider.crawler.stats.inc_value('httperror/response_ignored_status_count/%s' % response.status)
            logger.info( "Ignoring response %(response)r: HTTP status code is not handled or notallowed",{'response': response}, extra={'spider': spider},)
            return


