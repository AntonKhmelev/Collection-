import requests
from bs4 import BeautifulSoup
import lxml
from fake_headers import Headers

header = Headers(headers=True).generate()

url = 'https://www.superjob.ru/vacancy/search/?keywords=Analyst&geo%5Bt%5D%5B0%5D=4'

pages = [1, 2, 3]

siteName = 'hh'

for i in pages:
    page_url = url.format(i)
    response = requests.get(page_url, headers=header)
    soup = BeautifulSoup(response.text, 'lxml')
    names = [i.text for i in soup.find_all(class_='_1h3Zg _2rfUm _2hCDz _21a7u')]
    salary = [i.text for i in soup.find_all(class_='_1h3Zg _2Wp8I _2rfUm _2hCDz _2ZsgW')]
    print(names)
    print(salary)

    break

