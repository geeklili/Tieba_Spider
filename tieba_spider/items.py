# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    img_list = scrapy.Field()
    img_path = scrapy.Field()
    # pass
