# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import re


#class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
'''
    product_name = scrapy.Field()
    product_sale_price = scrapy.Field()
    product_category = scrapy.Field()
    product_original_price = scrapy.Field()
    product_availability = scrapy.Field()
'''
class AmazonItem(scrapy.Item):
	# define the fields for your item here like:
	title_Product = scrapy.Field()
	link_Product = scrapy.Field()
	ASIN_Product = scrapy.Field()
	url_response = scrapy.Field()
