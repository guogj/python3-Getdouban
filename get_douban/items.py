# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetDoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    title = scrapy.Field()
    info = scrapy.Field()
    imgurl = scrapy.Field()
    star = scrapy.Field()
    discuss = scrapy.Field()
    discussNum = scrapy.Field()

