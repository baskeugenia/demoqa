from pages.base_page import BasePage
from components.components import WebElement


class AccordianPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)
        self.s_content = WebElement(driver, '#section1Content > p')
        self.s2_content_1 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.s2_content_2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.s3_content = WebElement(driver, '#section3Content > p')
        self.s_heading = WebElement(driver, '#section1Heading')
