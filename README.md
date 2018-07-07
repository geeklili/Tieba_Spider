# tieba_spider
爬取某个贴吧里所有的图片

* 选择贴吧
* 获取贴吧的地址，并寻找规律，找出下一页的地址
* 获取帖子的地址
* 获取帖子下一页的地址
* 获取帖子里图片的地址

* 创建项目：scrapy startproject tieba_spider
* 创建爬虫：scrapy genspider tieba_go baidu.com