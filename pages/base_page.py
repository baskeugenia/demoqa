from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self, page=''):
        self.driver.get(self.base_url + page)

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        return self.get_url() == self.base_url
