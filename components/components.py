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

    def find_elements(self):
        try:
            print('-'*100, self.locator)
            elems = self.driver.find_elements(By.CSS_SELECTOR, self.locator)
        except NoSuchElementException:
            print('NO ELEMENTS')
            return False
        else:
            return elems

    def check_count_elements(self, count: int) -> bool:
        return len(self.find_elements()) == count

    def exist(self):
        return self.find_element()

    def click(self):
        self.find_element().click()

    def get_text(self):
        return str(self.find_element().text)

    def visible(self):
        return self.find_element().is_displayed()

    def is_displayed(self):
        return self.find_element().is_displayed()

    def send_keys(self, text: str):
        self.find_element().send_keys(text)