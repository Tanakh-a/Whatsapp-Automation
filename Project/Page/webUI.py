from _pytest import unittest
from selenium.webdriver.common.keys import Keys
from Locators.locators import locators

unittest.sortTestMethodsUsing = None


class appUI():

    def __init__(self, driver):  # constructor for calling object each time
        self.driver = driver

        self.search_box_xpath = locators.search_box_xpath
        self.search_click_xpath = locators.search_click_xpath
        self.message_box_xpath = locators.message_box_xpath
        self.menu_xpath = locators.menu_xpath
        self.logout_xpath = locators.logout_xpath

    def input_search(self, name):
        self.driver.find_element_by_xpath(self.search_box_xpath).send_keys(name)
        self.driver.find_element_by_xpath(self.search_click_xpath).click()

    def send_message(self, message):
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(self.message_box_xpath).send_keys(message)
        self.driver.find_element_by_xpath(self.message_box_xpath).send_keys(Keys.ENTER)

    def click_logout(self):
        self.driver.find_element_by_xpath(self.menu_xpath).click()
        self.driver.find_element_by_xpath(self.logout_xpath).click()
