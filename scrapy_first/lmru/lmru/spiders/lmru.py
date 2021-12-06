import scrapy
from scrapy.http import HtmlResponse
from lmru.items import LmruItem
from scrapy.loader import ItemLoader


class LmruSpider (scrapy.Spider):
    name = "lmru"
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, mark):
       self.start_urls = [f'https://leroymerlin.ru/search/?q={mark}']

    def parse(self, response: HtmlResponse):
       ads_links = response.xpath('//a[@class="bex6mjh_plp b1f5t594_plp iypgduq_plp nf842wf_plp"]/@href').extract()
        for link in ads_links:
            yield response.follow(link, callback=self.parse_ads)


    def parse_ads(self, response: HtmlResponse):
       name = response.css('div.c155f0re_plp c1pkpd8l_plp largeCard span.t9jup0e_plp p1h8lbu4_plp::text').extract.first()
       photos = response.xpath(//div[contains(@class, "s6jzgag_plp")]//div[contains(@class, "gp10zxbd6_plp")]/@data-url'
       price = response.xpath(//div[@class ="t3y6ha_plp xc1n09g_plp p1q9hgmc_plp"][1]/text()').extract()

       yield LmruItem(name=name, photos=photos, price=price)
       print(name, photos, price)

