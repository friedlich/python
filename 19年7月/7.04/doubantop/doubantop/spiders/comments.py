import scrapy,bs4
from ..items import DoubantopItem

class DoubantopSpider(scrapy.Spider):
    name = 'doubantop'
    allowed_domains = ['book.douban.com']
    start_urls = []
    for x in range(2):
        url = 'https://book.douban.com/top250?start=' + str(x * 25)
        start_urls.append(url)

    def parse(self, response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        datas = soup.find_all('tr',class_='item')
        for data in datas:
            book_url = data.find_all('a')[1]['href']
            comment_url = book_url+'comments/'
            yield scrapy.Request(comment_url,callback=self.parse_comment)

    def parse_comment(self,response):
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        book_name = soup.find('div',id='content').text.split()[0]
        datas = soup.find_all('div',class_='comment')
        for data in datas:
            item = DoubantopItem()
            item['book_name'] = book_name
            item['ID_name'] = data.find_all('a')[1].text
            item['comment'] = data.find('span',class_='short').text
            yield item