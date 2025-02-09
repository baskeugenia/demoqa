from pages.elements_page import ElementsPage
import time


def test_is_visible_btn_sidebar(browser):
    el_page = ElementsPage(browser)
    el_page.visit()
    el_page.btn_sidebar_first.click()
    time.sleep(3)
    assert el_page.btn_sidebar_first_textbox.exist()
    el_page.btn_sidebar_first.click()
    time.sleep(3)
    assert el_page.btn_sidebar_first_textbox.visible()
    el_page.btn_sidebar_first.click()
    time.sleep(3)
    assert not el_page.btn_sidebar_first_textbox.visible()




