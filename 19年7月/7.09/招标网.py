import time
from selenium import webdriver
import urllib.request
import csv
from bs4 import BeautifulSoup

def get_contents(url,content):
    driver.get(url)
    xml = driver.page_source
    # soup = BeautifulSoup(xml, 'lxml')
    soup = BeautifulSoup(xml, 'html.parser')
    trs = soup.find_all('tr')
    for tr in trs:
        ui = []
        tds=tr.find_all('td')
        for td in tds:
            ui.append(td.text.replace('\n','').replace(' ',''))
        content.append(ui)
    print(content)

def save_contents(content):
    with open(r'c:\Users\asus\Desktop\Python\风变Python爬虫精进\爬虫阶段练习\19年7月\7.09\test_3.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for i in content:
            writer.writerow(i)

if __name__ == '__main__':
    # opt = webdriver.ChromeOptions()
    # opt.set_headless()
    # driver = webdriver.Chrome(options=opt)
    # driver.maximize_window()
    driver = webdriver.Chrome()
    driver.maximize_window()
    content=[]
    url = 'http://ggggjy.gxgg.gov.cn:9005/zbxx/002003/002003001/002003001004/20190705/022301ec-de05-46af-bf67-48fda566e759.html'
    get_contents(url,content)
    save_contents(content)