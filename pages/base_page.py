from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement

import logging


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.viewport = WebElement(driver, 'head > meta')

    def visit(self, page=''):
        self.driver.get(self.base_url + page)

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        return self.get_url() == self.base_url

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        return self.driver.title

    def alert(self):
        try:
            return self.driver.switch_to.alert
        except Exception as ex:
            logging.log(1, ex)
            return False
