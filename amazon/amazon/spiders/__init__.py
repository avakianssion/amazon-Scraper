# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from amazon.items import AmazonItem
import re
import sys
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

class AmazonProductSpider(scrapy.Spider):
	name = "AmazonDeals"
	allowed_domains = ["amazon.com"]

	#Use working product URL below
	start_urls = [
"https://www.amazon.com/s?k=mens+sunglasses&i=fashion-mens-accessories&crid=2X91SRACUXMGW&sprefix=mens+sun%2Caps%2C245&ref=nb_sb_ss_c_2_8"	]
	custom_settings = {
			'FEED_URI' : 'Asin_Titles.json',
			'FEED_FORMAT' : 'json'
	}

	def parse(self, response):
		Link = response.css('.a-text-normal').css('a::attr(href)').extract()
		Title = response.css('span.a-text-normal').css('::text').extract()

		# for each product, create an AmazonItem, populate the fields and yield the item
		for result in zip(Link,Title):
			item = AmazonItem()
			item['title_Product'] = result[1]
			item['link_Product'] = result[0]
			# extract ASIN from link
			ASIN = re.findall(r"(?<=dp/)[A-Z0-9]{10}",result[0])[0]
			item['ASIN_Product'] = ASIN
			item['url_response'] = response.url
			yield item