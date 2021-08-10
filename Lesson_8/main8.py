import requests
import zipfile
import io
import os
from bs4 import BeautifulSoup
import lxml
import shutil

#if os.path.exists('./data'):
 #   os.makedirs('./data')

zip_file_url = ['https://data.gov.ru/sites/default/files/data-20161230-structure-20161230_2.csv', 'https://data.gov.ru/sites/default/files/data-20161230-structure-20161230.csv']
for num, i in enumerate(zip_file_url):
    response = requests.get(i, stream=True)
    with open(f'data/{num}.csv', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
#z = zipfile.ZipFile(io.BytesIO(r.content))
#z.extractall("./data")



