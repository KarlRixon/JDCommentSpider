# 爬取京东商城商品评价

## 介绍

由于京东限制只能查看最多1000条评论，如果想爬取更多数据可以等生成新的评论数据后再次爬取，管道会过滤重复评论。
此外管道还过滤了“此用户未填写评价内容”等无意义评论数据。

## 使用方法

修改`setting.py`中相关配置，如`START_URL`中`productID`代表某个商品。
`mongod --dbpath XXXX`
启动MongoDB后再开一个cmd
`cd JDComments/`
`scrapy crawl spider`
刷新Robo 3T会发现爬取的数据存储到了DB中