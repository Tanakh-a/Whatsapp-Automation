from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import excelRead


driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
time.sleep(15)

def send_messege(contact_no,message):
    search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(contact_no)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[11]').click()
    time.sleep(2)

    message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
    message_box.send_keys("Sent from bot.Don't reply...")
    message_box.send_keys(Keys.ENTER)
    #print(message + "sent to" + contact_no)

#contact_no = "+8801677-196458"

send_messege(excelRead.contact_no,"Sent from bot.Don't reply...")
#driver.close()
