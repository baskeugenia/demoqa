from pages.base_page import BasePage
from components.components import WebElement


class TextBoxPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.user_name = WebElement(driver, '//*[@id="userName"]', 'xpath')
        self.current_address = WebElement(driver, '//*[@id="currentAddress"]', 'xpath')
        self.output_name = WebElement(driver, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[1]', 'xpath')
        self.output_current_address = WebElement(driver, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[2]', 'xpath')
        self.btn_submit = WebElement(driver, '#submit')