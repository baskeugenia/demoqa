from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.btns_submenu = WebElement(driver, '#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, '#app > header > a > img')

        self.btn_show_small = WebElement(driver, '#showSmallModal')
        self.btn_show_large = WebElement(driver, '#showLargeModal')
        self.icon_close = WebElement(driver, '/html/body/div[4]/div/div/div[1]/button/span[1]', 'xpath')
