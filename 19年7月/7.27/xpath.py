from selenium import webdriver
import time

driver = webdriver.Chrome() #我的火狐浏览器没有驱动，所以是打不开的
driver.get('https://www.baidu.com')
# //*[@id="kw"]
time.sleep(2)
driver.find_element_by_xpath('//*[@id="u1"]/a[3]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="sole-input"]').send_keys('松江大学城')
driver.find_element_by_xpath('//*[@id="search-button"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="card-1"]/div/ul/li[1]/div[1]/div[3]/div[1]/span[1]/a').click()
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
# driver.find_element_by_id('kw').send_keys('python')
# driver.find_element_by_xpath('//*[@id="su"]').click()
# driver.find_element_by_xpath('//*[@id="s_xmancard_news"]/div/div[1]/div/a/span[2]').click()
# driver.find_element_by_xpath('//*[@id="s_xmancard_news"]/div/div[1]/div/div/a').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[3]/ul/li[1]/a[2]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/table/tbody/tr[4]/td[2]/a[1]').click()
time.sleep(2)
driver.close()

# //*[@id="s_menus_wrapper"]/span[2]  导航
# //*[@id="s_menus_wrapper"]/span[1]  推荐
# //*[@id="s_xmancard_news"]/div/div[1]/div/div/a 实时热点
# //*[@id="s_xmancard_news"]/div/div[1]/div/a/span[2] 换一换

# //*[@id="main"]/div[1]/div[3]/ul/li[1]/a[2] 爱情
## //*[@id="main-nav"]/li[7]/a 汽车
# //*[@id="main"]/div[2]/div/table/tbody/tr[4]/td[2]/a[1] 致我们终将逝去的青春
