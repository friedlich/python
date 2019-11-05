import requests
import re
import json
import os

# 设计模式 -- 面向对象
class Spider(object):
    def start_request(self):
        # 1. 找到所有英雄的英文名
        text = requests.get("https://lol.qq.com/biz/hero/champion.js").text
        content = re.findall(r'LOLherojs.champion=(.+?);', text)[0] # 处理成正确的json数据
        py_data = json.loads(content) # json数据转化为Python数据类型
        es_name = list(py_data['keys'].values())
        self.next_request(es_name)

    def next_request(self, es_name):
        for e_name in es_name:
            # 2. 取英雄皮肤ID
            text = requests.get("https://lol.qq.com/biz/hero/%s.js" % e_name).text
            content = re.findall(r'champion.%s=(.+?);'% e_name, text)[0] # 处理成正确的json数据
            py_data = json.loads(content) # json数据转化为Python数据类型
            hero_name = py_data['data']['name']
            if os.path.exists(hero_name) == False:
                os.mkdir(hero_name)

            for skin in py_data['data']['skins']:
                skin_id = skin['id']
                skin_name = skin['name']

                # 3. 下载皮肤
                content = requests.get("http://ossweb-img.qq.com/images/lol/web201310/skin/big%s.jpg" % skin_id).content
                # 4. 保存皮肤
                fileName = hero_name + "\\" +skin_name + ".jpg"
                print("正在保存圖片文件：" + fileName)
                try:
                    with open(fileName, "wb") as f:
                        f.write(content)
                except:
                    pass

spider = Spider()
spider.start_request()