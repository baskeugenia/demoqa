from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    demoqa = DemoQa(browser)
    demoqa.visit()
    demoqa.btn_element.click()
    demoqa.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    el_page = ElementsPage(browser)
    assert el_page.equal_url()