import requests
#from bs4 import BeautifulSoup
from lxml import html
from fake_headers import Headers
#import csv
#import pandas as pd

header = Headers(headers=True).generate()

paths2 = ['//*[@id="index_page"]/div[7]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/span[2]/a/span/text()',
          '//*[@id="index_page"]/div[7]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/span[2]/text()',
          '//*[@id="index_page"]/div[7]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/span[1]/text()',
          '//*[@id="index_page"]/div[7]/div[2]/div[3]/div/div/div/div[1]/div/div[2]/span[2]/span/text()',
          '//*[@id="index_page"]/div[7]/div[2]/div[3]/div/div/div/div[1]/div/div[2]/div/span[2]/text()',
          '//*[@id="index_page"]/div[7]/div[2]/div[3]/div/div/div/div[1]/div/div[2]/div/span[1]/text()']



url2 = 'https://news.mail.ru/'

response2 = requests.get(url2, headers=header)

parsed2 = html.fromstring(response2.text)

for n in paths2:
    result2 = parsed2.xpath(n)[0]
    print(result2)



