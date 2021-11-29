from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from avru import settings
from avru.spiders.avru import AvruSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(AvruSpider, mark-'asus')
    process.start()


