# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class Jobui2Pipeline(object):
#     def process_item(self, item, spider):
#         return item

import openpyxl

class Jobui2Pipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['公司', '职位', '地址', '招聘信息'])

    def process_item(self,item,spider):
        line = [item['company'],item['position'],item['address'],item['detail']]
        self.ws.append(line)
        return item

    def close_spider(self,spider):
        self.wb.save('./jobui4.xlsx')
        self.wb.close()






