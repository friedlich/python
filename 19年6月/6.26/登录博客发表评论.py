from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://wordpress-edu-3autumn.localprod.forc.work/wp-login.php')
time.sleep(2)

address = driver.find_element_by_id('user_login')
address.send_keys(input('请输入用户名：')) # spiderman
password = driver.find_element_by_id('user_pass')
password.send_keys('crawler334566')
button = driver.find_element_by_id('wp-submit')
button.click()
time.sleep(2)

title3 = driver.find_element_by_id('post-20').find_element_by_link_text('未来已来（三）——同九义何汝秀')
title3.click()
time.sleep(2)

comment = driver.find_element_by_id('respond').find_element_by_tag_name('textarea')
comment.send_keys(input('请输入评论：'))
button = driver.find_element_by_class_name('form-submit').find_element_by_name('submit')
button.click()

driver.close()
