from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2) # 这里不加的话网页是转不过来的，会报错，必须要有缓冲时间

teacher = driver.find_element_by_id('teacher')
teacher.send_keys('吴枫')
assistants = driver.find_element_by_id('assistant')
assistants.send_keys('都喜欢')
button = driver.find_element_by_class_name('sub')
button.click()
time.sleep(2)

sentences = driver.find_elements_by_class_name('content')
for sentence in sentences:
    title = sentence.find_element_by_tag_name('h1').text
    print(type(title))
    content = sentence.find_element_by_id('p').text.strip()
    print(type(content))
    print(title + '\n' + content + '\n')

driver.close()
