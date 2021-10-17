import HtmlTestRunner
from selenium import webdriver
import unittest
import time
import sys
import os
# sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Page.webUI import appUI
from Excel.write_in_excel import successfullySent
from Excel.read_data import dataRead


class testUI(unittest.TestCase):
    driver = webdriver.Chrome(executable_path="C:/browserdriver/chromedriver.exe")

    @classmethod
    def setUp(cls):
        cls.driver.implicitly_wait(5)

    def testALogin_01(self):
        driver = self.driver
        driver.get('https://web.whatsapp.com/')
        time.sleep(5)
        self.driver.implicitly_wait(10)

    def testBSearchNumber_02(self):
        # print("search")
        driver = self.driver
        read = dataRead()
        name = read.contact()
        # print(name)
        search = appUI(driver)
        search.input_search(name)
        self.driver.implicitly_wait(2)

    def testCMessageSending_03(self):
        # print('text')
        self.driver.implicitly_wait(15)
        driver = self.driver
        text = appUI(driver)
        text.send_message('Sent for testing purpose')
        time.sleep(5)

    def testDSent_04(self):
        # print("sentmsg")
        # writeSent = successfullySent()
        # writeSent.write_sent()
        ins = successfullySent()
        ins.update_ws()

    def testELogout_05(self):
        self.driver.implicitly_wait(10)
        driver = self.driver
        logout = appUI(driver)
        logout.click_logout()

    @classmethod
    def tearDownClass_06(cls):
        cls.driver.quit()
        print('Test completed')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='E:/Project/Report'))
