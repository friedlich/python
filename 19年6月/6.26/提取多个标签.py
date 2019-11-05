from selenium import webdriver
import time

driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器

driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)
labels = driver.find_elements_by_tag_name('label')
print(type(labels))
# print(labels.text)  AttributeError: 'list' object has no attribute 'text'
print(labels)
for label in labels:
    print(label.text)
teacher = driver.find_element_by_class_name('teacher')
print(teacher.get_attribute('type'))
driver.close()
