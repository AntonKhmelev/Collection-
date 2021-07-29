import scrapy
from scrapy.http import HtmlResponse
from avru.items import AvruItem
from scrapy.loader import ItemLoader


class AvruSpider (scrapy.Spider):
    name = "avru"
    allowed_domains = ['avito.ru']

    def __init__(self, mark):
       self.start_urls = [f'https://www.avito.ru/rossiya/bytovaya_elektronika?q={mark}']

    def parse(self, response: HtmlResponse):
       ads_links = response.xpath('//a[@class="snippet-link"]/@href').extract()
        for link in ads_links:
            yield response.follow(link, callback=self.parse_ads)
