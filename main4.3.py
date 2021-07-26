import requests
#from bs4 import BeautifulSoup
from lxml import html
from fake_headers import Headers
#import csv
#import pandas as pd

header = Headers(headers=True).generate()

paths3 = ['//*[@id="more"]/div[1]/div[2]/h3/a/text()',
          '//*[@id="more"]/div[1]/div[1]/span/text()',
          '//*[@id="more"]/div[2]/div[2]/h3/a/text()',
          '//*[@id="more"]/div[2]/div[1]/span/text()']



url3 = 'https://lenta.ru/parts/news/'

response3 = requests.get(url3, headers=header)

parsed3 = html.fromstring(response3.text)

for k in paths3:
    result3 = parsed3.xpath(k)[0]
    print(result3)



