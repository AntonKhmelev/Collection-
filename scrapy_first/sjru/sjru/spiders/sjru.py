import scrapy
from scrapy.http import HtmlResponse
from sjru.items import SjruItem


class SjruSpider (scrapy.Spider):
    name = "sjru"
    allowed_domains = ['superjob.ru']
    start_urls = ['https://www.superjob.ru/vacancy/search/?keywords=python&geo%5Bt%5D%5B0%5D=4']

    def parse(self, response: HtmlResponse):
    next_page = response.css('a.icMQ_ bs_sM _3ze9n _3fOgw f-test-button-dalshe f-test-link-Dalshe::attr(href)').extract_first()
    yield response.follow(next_page, callback=self.parse)

    vacansy = response.css('div.f-test-search-result-item div._2G1F a.icMQ_ _2JivQ _1UJAN::attr(href)').extract()

    for link in vacansy:
        yield response.follow(link, callback=self.vacansy_parse)


    def vacansy_parse(self, response: HtmlResponse):
        name = response.css('div._1h3Zg _2rfUm _2hCDz _21a7u::text').extract_first()
        salary = response.css('span._1h3Zg _2Wp8I _2rfUm _2hCDz _2ZsgW::text').extract()
        reference = response.css('a.icMQ_ _2JivQ _1UJAN::attr(href)').extract_first() # ссылка на вакансию
        employer = response.css('a.icMQ_ _205Zx _25-u7::attr(href)').extract_first() # ссылка на источник (работодателя)
        yield HhruItem(name=name, salary=salary, reference=reference, employer=employer)