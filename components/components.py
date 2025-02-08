from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebElement:

    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def find_element(self):
        try:
            print('-'*100, self.locator)
            elem = self.driver.find_element(By.CSS_SELECTOR, self.locator)
        except NoSuchElementException:
            print('NO ELEMENT')
            return False
        else:
            return elem

    def exist(self):
        return self.find_element()

    def click(self):
        self.find_element().click()

    def get_text(self):
        return str(self.find_element().text)
