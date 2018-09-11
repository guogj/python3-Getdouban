# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from get_douban.settings import mongo_db_name,mongo_db_collection

class GetDoubanPipeline(object):
    def __init__(self):
        dbname = mongo_db_name
        sheetname = mongo_db_collection
        myclient = MongoClient('mongodb://localhost:27017/')
        mydb = myclient[dbname]
        self.post = mydb[sheetname]

    total = 0

    def open_spider(self, spider):
        print("open spider ...")

    def process_item(self, item, spider):
        data = dict(item)
        # 已经存在的标题不在存储到mongo
        title = self.post.find_one({'title': data['title']})
        if title is None:
            self.post.insert(data)
        self.total += 1  # 累计文章数
        # 显示基本数据内容，通常可以在这个方法中对数据保存入库、触发分析动作等
        # print("%s %s %s %s" % (item['title'],item['info'],item['star'],item['imgurl']))
        return item

    def close_spider(self, spider):
        # 作为示例，这里只是显示处理结果
        print(u"共", self.total, u"篇文章")
        print("close spider ...")
