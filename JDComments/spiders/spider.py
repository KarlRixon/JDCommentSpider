# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.utils.project import get_project_settings
from scrapy.http import Request
from ..items import JdcommentsItem
import json

class SpiderSpider(Spider):
    name = 'spider'
    allowed_domains = ['jd.com']
    settings = get_project_settings()
    start_urls = [settings['START_URL']]
    max_page = settings['MAX_PAGE']

    def parse(self, response):
        for page in range(0, self.max_page):
            url = self.start_urls[0].format(str(page))
            yield Request(url=url, callback=self.parse_comment)

    @staticmethod
    def parse_comment(response):
        try:
            comment_json = json.loads(response.text)
        except json.decoder.JSONDecodeError:
            return

        for com in comment_json['comments']:
            item = JdcommentsItem()
            item['user_name'] = com['nickname']
            item['comment_star'] = com['score']
            item['comment_con'] = com['content']
            item['comment_time'] = com['creationTime']
            item['comment_id'] = com['id']
            yield item