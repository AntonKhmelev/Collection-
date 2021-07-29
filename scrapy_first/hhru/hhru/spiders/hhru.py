import scrapy
from scrapy.http import HtmlResponse
from hhru.items import HhruItem


class HhruSpider (scrapy.Spider):
    name = "hhru"
    allowed_domains = ['hh.ru']
    start_urls = ['https://izhevsk.hh.ru/search/vacancy?area=&st=searchVacancy&text=python']

    def parse(self, response: HtmlResponse):
    next_page = response.css('div.bloko-gap bloko-gap_top div.pager-block a.bloko-button::attr(href)').extract_first()
    yield response.follow(next_page, callback=self.parse)

    vacansy = response.css('div.vacancy-serp div.vacancy-serp-item div.vacancy-serp-item__row_header a.bloko-link::attr(href)').extract()

    for link in vacansy:
        yield response.follow(link, callback=self.vacansy_parse)


    def vacansy_parse(self, response: HtmlResponse):
        name = response.css('div.vacancy-title h1.header::text').extract_first()
        salary = response.css('div.vacancy-title p.vacancy-salary::text').extract()
        reference = response.css('a.bloko-link::attr(href)').extract_first() # ссылка на вакансию
        employer = response.css('a.vacancy-serp__vacancy-employer-logo::attr(href)').extract_first() # ссылка на источник (работодателя)
        yield HhruItem(name=name, salary=salary, reference=reference, employer=employer)