import urllib.request
import urllib.parse
import urllib
from bs4 import BeautifulSoup

class Baike(object):
	def __init__(self,keyword='仙剑'):
		self.keyword = keyword
		self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

	def get_url(self):
		self.keyword = urllib.parse.quote(self.keyword)
		url = 'https://baike.baidu.com/item/%s' % self.keyword
		return url

	def downlaod_baidubaike_html(self,url):
		req = urllib.request.Request(url,headers=self.headers)
		res = urllib.request.urlopen(req)
		html = res.read().decode('utf-8')
		return html

	def html_parse(self,html):
		soup = BeautifulSoup(html,'html.parser')
		# title
		title = '查找关键字：%s\n\n' % soup.find('h1').text
		
		# 同义词和小标题 keyword
		keyword=''
		brief = soup.find('h2')
		sanme = soup.find('span',{'class':'view-tip-panel'})
		if brief:
			keyword = brief.text + '\n'
		if sanme:
			keyword += sanme.text + '\n'
		
		# 主要内容 content
		begin = '    '
		content = soup.find('div',{'class':'lemma-summary'})
		content = begin + content.text.replace('\n','')
		content += '\n'

		# 相关分词 participles列表
		participles = []
		parts = soup.findAll('h3',{'class':'title-text'})
		for part in parts:
			[s.extract() for s in part('span')]
			participles.append(part.text)

		
		return title,keyword,content,participles 			
