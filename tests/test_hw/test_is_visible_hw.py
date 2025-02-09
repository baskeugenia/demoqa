from pages.accordian_page import AccordianPage
import time


def test_is_visible_accordion(browser):
    ac_page = AccordianPage(browser)
    ac_page.visit()
    time.sleep(3)
    assert ac_page.s_content.visible()
    ac_page.s_heading.click()
    time.sleep(3)
    assert not ac_page.s_content.visible()


def test_is_visible_accodian_defalt(browser):
    ac_page = AccordianPage(browser)
    ac_page.visit()
    time.sleep(3)
    assert not ac_page.s2_content_2.visible()
    assert not ac_page.s2_content_1.visible()
    assert not ac_page.s3_content.visible()


