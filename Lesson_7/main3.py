from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#chromeCapabilities = selenium.Capabilities.chrome()


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#options.add_argument('--disable-extensions' '--disable-infobars' '--ignore-ssl-errors=yes' '--ignore-certificate-errors')
#browser = webdriver.Chrome(options=options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')
#driver.get('https://mail.ru')


#driver.

browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe')
browser.get('https://www.mvideo.ru/product-list-page?q=%D1%85%D0%B8%D1%82%D1%8B%20%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6')

#field_to_fill_name = browser.find_elements_by_class_name('q')

#field_to_fill_name.send_keys('event')
#field_to_fill_name.send_keys(Keys.ENTER)

all_events = browser.find_elements_by_xpath('//a[@class="product-title__text product-title--clamp"]')

#print(all_events)

for i in all_events:
    title = i.find_element_by_tag_name('href').text
    print(title.text)
    #if 'Event' in title:
        #date = i.find_element_by_tag_name('p').text
        #print('{} - {}'.format(title, date))
    


