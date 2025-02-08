from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
import time


def test_check_text_1(browser):
    dqa = DemoQa(browser)
    dqa.visit()
    ft = dqa.footer.get_text()
    assert ft == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    dqa.btn_element.click()
    time.sleep(3)
    el_page = ElementsPage(browser)
    assert el_page.div_elem.get_text() == 'Please select an item from left to start practice.'
