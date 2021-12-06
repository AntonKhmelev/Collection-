# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


#class ScrapyFirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
 #   pass

class JobparserItem(scrapy.Item):
    _id = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()

    pass