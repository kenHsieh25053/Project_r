# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings

# class BookCrawlerPipeline(object):
#     def process_item(self, item, spider):
#         return item

# 設定與mongodb連線並傳輸資料
class BookinfoPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        connection.close()

    def process_item(self, BookInfoItem, spider):
        self.collection.insert(dict(BookInfoItem))
        return BookInfoItem
