from selenium import webdriver
import allure
import pytest

class TestApp:
    def send_message(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://web.whatsapp.com/")
        self.driver.find_element_by_xpath()
        self.driver.close()
        #self.driver.maximize_window()
        #print(driver.title)

    #def test_messege(self):
