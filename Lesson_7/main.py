from selenium import webdriver
import time
#chromeCapabilities = selenium.Capabilities.chrome()


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
#options.add_argument('--disable-extensions' '--disable-infobars' '--ignore-ssl-errors=yes' '--ignore-certificate-errors')
#browser = webdriver.Chrome(options=options, executable_path=r'C:\Program Files (x86)\chromedriver.exe')
#driver.get('https://mail.ru')


#driver.

class Mailru:
    def __init__(self):
        #self.options = webdriver.ChromeOptions()
        #options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\chromedriver.exe')
        self.browser.get('https://mail.ru')



    def login(self, email, password):

        self.browser.find_element_by_xpath('//*[@id="mailbox"]/form[1]/div[1]/div[2]/input').send_keys(email)
        #self.browser.get('https://mail.ru')
        self.browser.find_element_by_xpath('//*[@id="mailbox"]/form[1]/div[1]/div[1]/select/option[5]').click()
        self.browser.find_element_by_xpath('//*[@id="mailbox"]/form[1]/button[1]').click()
        #self.browser.find_element_by_xpath('//*[@id="mailbox"]/form[1]/div[1]/div[1]/select').send_keys(password)
        self.browser.find_element_by_xpath('//*[@id="mailbox"]/form[1]/div[2]/input').send_keys(password)
        self.browser.find_element_by_xpath('//*[@id="mailbox"]/form[1]/button[2]').click()
    #def parse(self, author, date, topic, text_of):
        #self. browser.find_elements_by_xpath(//*[@id="app-canvas"]/div/div[1]/div[1]/div/div[2]/span/div[2]/div/div/div/div/div[1]/div/div/div[1]/div/div/div/div[4]).click()


if __name__ == '__main__':
    mail = Mailru()
    mail.login('ivantest', 'funfzig230')
    #mail.parse()



