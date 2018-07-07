# -*- coding: utf-8 -*-
import scrapy

from tieba_spider.items import TiebaSpiderItem


class TiebaGoSpider(scrapy.Spider):
    name = 'tieba_go'
    allowed_domains = ['baidu.com']
    url = 'https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&ie=utf-8&pn='
    index = 0
    start_urls = [url + str(index)]

    def parse(self, response):
        """处理贴吧页面"""
        # 拿到首页的返回值后，利用xpath提取到整个页面里所有的帖子的url列表
        page_list = response.xpath('//*[@class="threadlist_title pull_left j_th_tit "]/a/@href').extract()
        # print(page_list)
        # page_list: 为在某个贴吧的首页里的所有的帖子的url列表
        # page_list: ['/p/5783295716', '/p/5785832366',...]
        for page in page_list:
            page_url = 'http://tieba.baidu.com' + page

            # 向每个页面发起请求，并设定处理函数，把请求的返回值处理的任务甩给该函数
            yield scrapy.Request(url=page_url, callback=self.parse_page)

        # 处理下一页的数据
        self.index += 50
        next_page_url = self.url + str(self.index)
        # 把锅甩给自己
        yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_page(self, response):
        """处理帖子页面"""
        item = TiebaSpiderItem()
        # 获取到帖子页面里的图片url，并交给item，这样接下来管道文件就可以提取item里的url，下载图片了
        item['img_list'] = response.xpath('//*[@class="BDE_Image"]/@src').extract()
        print(item)

        # 查看贴子如果有很多页，就获取帖子里的下一页的地址
        next_page_url = response.xpath('//ul[@class="l_posts_num"]/li[1]/a[last()-1]/@href').extract_first()
        # print(next_page_url,'='*20)
        # next_page_url : /p/5771989602?pn=2
        next_page_url = 'https://tieba.baidu.com' + next_page_url
        # 把锅甩给自己
        yield scrapy.Request(url=next_page_url, callback=self.parse_page)