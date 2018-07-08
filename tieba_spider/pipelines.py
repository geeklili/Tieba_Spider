# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 既然是处理图片信息，就应该导入处理图片的管道类
import scrapy
from scrapy.pipelines.images import ImagesPipeline


# 调整继承关系
# 参考教程：http://wiki.jikexueyuan.com/project/scrapy/download-picture.html
from tieba_spider.settings import IMAGES_STORE


class TiebaSpiderPipeline(ImagesPipeline):
    # 在工作流程中可以看到，管道会得到图片的 URL 并从项目中下载。为了这么做，
    # 你需要重写 get_media_requests()方法，并对各个图片 URL 返回一个 Request
    # def get_media_requests(self, item, info):
    #     return [Request(x) for x in item.get(self.images_urls_field, [])]

    def get_media_requests(self, item, info):
        # 向每个url发送请求,即是下载该图片
        return [scrapy.Request(x) for x in item.get('img_list', [])]

    # 另外一种繁琐点的方法，注意图片如果下载不成功，考虑是不是http的问题
    # def get_media_requests(self,item,info):
    #     image_url = item['page_list']
    #     for img in image_url:
    #         img = img.replace('http','https')
    #         yield scrapy.Request(img)

    # 图片下载完成后, 或者不成功,都会将信息都会调用item_completed这个函数,
    # 并把值赋给result,并返回给函数item_completed,以下为result得值:
    # [(True,
    #   {'checksum': '2b00042f7481c7b056c4b410d28f33cf',
    #    'path': 'full/7d97e98f8af710c7e7fe703abc8f639e0ee507c4.jpg',
    #    'url': 'http://www.example.com/images/product1.jpg'}),
    #  (True,
    #   {'checksum': 'b9628c4ab9b595f72f280b90c4fd093d',
    #    'path': 'full/1ca5879492b8fd606df1964ea3c1e2f4520f076f.jpg',
    #    'url': 'http://www.example.com/images/product2.jpg'}),
    #  (False,
    #   Failure(...))]

    # def item_completed(self, results, item, info):
    #     if isinstance(item, dict) or self.images_result_field in item.fields:
    #         item[self.images_result_field] = [x for ok, x in results if ok]
    #     return item

    def item_completed(self, results, item, info):
        """图片下载完成后的后续操作,可以获得图片的名字,路径"""
        img_path = [x['path'] for ok, x in results if ok]
        if img_path:
            item['img_path'] = [IMAGES_STORE + i for i in img_path]
            # print(item)
            # print('='*100)
        return item
