from bs4 import BeautifulSoup
from selenium import webdriver
import requests,csv,time,lxml

driver = webdriver.Chrome()

page = 0
for i in range(1):
    page += 1
    url = "https://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"
    driver.get(url.format(page=page))
    time.sleep(2)
    pageSource = driver.page_source
    html = BeautifulSoup(pageSource,'html.parser') 
    house_list = html.find(class_="list").find_all('li')
    for house in house_list:
        infor = house.find('h2').text
        print(infor)






