import scrapy
import bs4
from ..items import DangdangItem

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_damains = ['bang.dangdang.com']
    start_urls = []
    for i in range(1,4):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-' + str(i)
        start_urls.append(url)

    def parse(self,response):
        bs = bs4.BeautifulSoup(response.text,'html.parser')
        datas = bs.find(class_='bang_list').find_all('li')
        for data in datas:
            item = DangdangItem()
            item['title'] = data.find(class_="name").text
            item['author'] = data.find(class_="publisher_info").text
            item['price'] = data.find(class_="price").find(class_="price_n").text
            yield item

