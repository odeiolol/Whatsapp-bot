from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


#create a new tab of chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
#open a link on this tab
driver.get("https://web.whatsapp.com/")

time.sleep(10)

#contact name
contato = ['Cheese']
#message you want to send
mensage= 'bora jogar'


#defs

#find contact element of whatsapp
def find_contact(contato):
    serchC= driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(1)
    serchC.click()
    serchC.send_keys(contato)
    serchC.send_keys(Keys.ENTER)

#find text element to send the message 
def mensagem(mensage):
    mes= driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    mes[1].click()
    time.sleep(1)
    mes[1].send_keys(mensage)
    mes[1].send_keys(Keys.ENTER)


#and do sttuf
while True:
    
    find_contact(contato)
    mensagem(mensage)
    time.sleep(297)

