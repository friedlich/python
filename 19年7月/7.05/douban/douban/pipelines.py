# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class DoubanPipeline(object):
#     def process_item(self, item, spider):
#         return item

import openpyxl

class DoubanPipeline(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.append(['书名','ID名', '短评'])

    def process_item(self, item, spider):
        line = [item['book_name'],item['ID_name'], item['comment']]
        self.ws.append(line)
        return item

    def close_spider(self, spider):
        self.wb.save('book1.xlsx')
        self.wb.close()
