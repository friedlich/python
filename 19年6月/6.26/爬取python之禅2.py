from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()

driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)

teacher = driver.find_element_by_id('teacher')
teacher.send_keys('只有吴枫呀')
assistant = driver.find_element_by_id('assistant')
assistant.send_keys('卡西助教呀')
button = driver.find_element_by_class_name('sub')
button.click()
time.sleep(1)

pageSource = driver.page_source
print(type(pageSource))
be = BeautifulSoup(pageSource,'html.parser')
sentences = be.find_all(class_='content')
print(type(sentences))
for sentence in sentences:
    title = sentence.find('h1').text
    print(type(title))
    content = sentence.find(id='p').text.strip()
    print(type(content))
    print(title + '\n' + content + '\n')

driver.close()