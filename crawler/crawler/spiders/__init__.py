# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy import Spider, Request, Item
import redis


class StackOverflowSpider(Spider):
    name = 'stackoverflow'

    start_urls = ['https://stackoverflow.com/jobs/remote-developer-jobs']

    def __init__(self, name=None, **kwargs):
        super(StackOverflowSpider, self).__init__(name=None, **kwargs)
        self.redis_db = redis.StrictRedis(host='localhost', port=6379)
        keys = self.redis_db.keys('so:*')
        for key in keys:
            self.redis_db.delete(key)

    def parse(self, response):
        for item_selector in response.css('div.-job-item'):
            for tag in item_selector.css('div.-tags a.post-tag::text').extract():
                self.redis_db.incr('so:' + tag)

        next_page = response.css('div.pagination a.test-pagination-next::attr(href)').extract_first()
        if next_page:
            yield Request(response.urljoin(next_page), callback=self.parse)
