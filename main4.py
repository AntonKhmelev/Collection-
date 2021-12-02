import requests
#from bs4 import BeautifulSoup
from lxml import html
from fake_headers import Headers
#import csv
#import pandas as pd

header = Headers(headers=True).generate()

paths = ['//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[1]/article/div[2]/a/h2/text()',
'//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[1]/article/div[2]/div[2]/div[1]/div/span[1]/a/text()',
'//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[1]/article/div[2]/div[2]/div[1]/div/span[2]/text()',
'//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[2]/article/div[1]/div/a/h2/text()',
'//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[2]/article/div[3]/div[1]/div/span[1]/a/text()',
'//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[2]/article/div[3]/div[1]/div/span[2]/text()',
'//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[3]/article/div[1]/div/a/h2/text()',
'//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[3]/article/div[3]/div[1]/div/span[1]/a/text()',
'//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[3]/article/div[3]/div[1]/div/span[2]/text()',
'//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[4]/article/div[1]/div/a/h2/text()',
'//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[4]/article/div[3]/div[1]/div/span[1]/a/text()',
'//*[@id="neo-page"]/div/div[2]/div/div[1]/div[1]/div[4]/article/div[3]/div[1]/div/span[2]/text()']
#'//*[@id="neo-page"]/div/div[2]/div/div[1]/article/div[1]/a/.attribute["href"].value']


url = 'https://yandex.ru/news/'

response = requests.get(url, headers=header)

parsed = html.fromstring(response.text)

for i in paths:
    result = parsed.xpath(i)[0]
    print(result)




