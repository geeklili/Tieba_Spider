# -*- coding: utf-8 -*-
import scrapy


class TiebaGoSpider(scrapy.Spider):
    name = 'tieba_go'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
