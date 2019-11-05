from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html')
time.sleep(2)

button = driver.find_element_by_class_name('js_get_more_hot')
button.click()
time.sleep(2)

comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li')
print(len(comments))
for comment in comments:    
    sweet = comment.find_element_by_tag_name('p')
    print('评论：{}\n---\n'.format(sweet.text))

driver.close()


# driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html') # 访问页面
# time.sleep(2)

# button = driver.find_element_by_class_name('js_get_more_hot') # 根据类名找到【点击加载更多】
# button.click() # 点击
# time.sleep(2) # 等待两秒

# comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') #  使用class_name找到评论
# print(len(comments)) # 打印获取到的评论个数
# for comment in comments: # 遍历列表
#     sweet = comment.find_element_by_tag_name('p') # 找到评论
#     print ('评论：%s\n ---\n'%sweet.text) # 打印评论
# driver.close() # 关闭浏览器

