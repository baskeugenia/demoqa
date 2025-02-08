from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time


def test_go_to_page_elements(browser):
    dqa_page = DemoQa(browser)
    dqa_page.visit()
    time.sleep(3)
    assert dqa_page.equal_url()
    el_page = ElementsPage(browser)
    dqa_page.btn_element.click()
    assert el_page.equal_url()
