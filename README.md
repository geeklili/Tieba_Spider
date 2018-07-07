# tieba_spider
爬取某个贴吧里所有的图片


* 创建项目：scrapy startproject tieba_spider
* 创建爬虫：scrapy genspider tieba_go baidu.com

tieba_go.py:
* 选择贴吧
* 获取贴吧的地址，并寻找规律，找出下一页的地址
* 获取帖子的地址
* 获取帖子下一页的地址
* 获取帖子里图片的地址

settings.py
* 配置文件，请求头，代理，文件储存位置，robot协议，管道文件

pipelines.py
* 写一个下载图片的中间件，重写两个函数：get_media_requests，item_completed
* get_media_requests：向图片的url发送请求
* item_completed：处理请求后的事，如获取图片的路径

items.py
* 定义需求的字段

### 项目启动：
1. 进入到项目目录
2. scrapy crawl spider