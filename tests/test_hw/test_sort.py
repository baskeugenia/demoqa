import time
from pages.webtables_page import WebtablesPage
from selenium.webdriver.common.keys import Keys


def test_sort(browser):
    wp = WebtablesPage(browser)
    wp.visit()

    wp.email.click_force()
    time.sleep(3)

    assert wp.sort_asc_by_email.exist()

    wp.email.click_force()
    time.sleep(3)

    assert wp.sort_desc_by_email.exist()