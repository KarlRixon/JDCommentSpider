# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy.exceptions import DropItem

from .settings import MONGODB_SERVER, MONGODB_PORT, MONGODB_DB, MONGODB_COLLECTION

class JdcommentsPipeline(object):
    def __init__(self):
        host = MONGODB_SERVER
        port = MONGODB_PORT
        db_name = MONGODB_DB
        client = MongoClient(host=host, port=port)
        db=client[db_name]
        self.collection = db[MONGODB_COLLECTION]

    def process_item(self, item, spider):
        if self.collection.find_one({'comment_id':item['comment_id']}):
            raise DropItem('%s, %s is exist!' % (item['comment_id'], item['comment_time']))
        elif item['comment_con'] == '此用户未填写评价内容':
            raise DropItem('%s, %s is worthless!' % (item['comment_id'], item['comment_time']))
        else:
            self.collection.insert(dict(item))
        return item
