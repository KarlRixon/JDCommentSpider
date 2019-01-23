# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class JdcommentsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    user_name = Field()
    comment_star = Field()
    comment_con = Field()
    comment_time = Field()
    comment_id = Field()
    
