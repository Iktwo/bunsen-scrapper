# -*- coding: utf-8 -*-
import scrapy

from bunsenscrapper.items import BunsenscrapperItem
from scrapy.http.request import Request

class BunsenSpider(scrapy.Spider):
    name = "bunsen"
    allowed_domains = ["bunsencomics.com"]
    start_urls = (
        'http://www.bunsencomics.com/?category=Bunsen+C%C3%B3mics',
    )

    def parse(self, response):
	for sel in response.xpath('//article'):
		item = BunsenscrapperItem()
		item['title'] = sel.xpath('h1/a/text()').extract()
		item['link'] = sel.xpath('h1/a/@href').extract()
		item['img'] = sel.css('.thumb-image').xpath('@data-src').extract()
		yield item
        pass
	next_link = response.xpath('//a[contains(text(), "Older")]/@href').extract()
	if next_link:
		yield Request('http://www.bunsencomics.com' + next_link[0], self.parse)
