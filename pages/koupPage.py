from pages.base_page import BasePage
from components.components import WebElement


class KoupPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/'
        super().__init__(driver, self.base_url)

        self.link_add = WebElement(driver, '//*[@id="content"]/ul/li[2]/a', 'xpath')