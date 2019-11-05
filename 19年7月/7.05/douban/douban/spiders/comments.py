import scrapy,bs4
from ..items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['book.douban.com']
    start_urls = []
    for i in range(2):
        url = 'https://book.douban.com/top250?start=' + str(i*25)
        start_urls.append(url)

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        datas = soup.find_all(class_="pl2")
        for data in datas:
            book_url = data.find('a')['href']
            comment_url = book_url+'comments/'
            yield scrapy.Request(comment_url,callback=self.parse_comment)

    def parse_comment(self,response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        book_name = soup.find(id="content").text.split()[0]
        datas = soup.find_all(class_="comment")
        for data in datas:
            item = DoubanItem()
            item['book_name'] = book_name
            item['ID_name'] = data.find_all('a')[1].text
            item['comment'] = data.find(class_='short').text
            yield item

