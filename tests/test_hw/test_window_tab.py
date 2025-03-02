import time
from pages.links_page import LinksPage


def test_window_tab(browser):
    lp = LinksPage(browser)
    lp.visit()

    assert len(browser.window_handles) == 1

    lp.link_home.click()
    time.sleep(2)

    assert len(browser.window_handles) == 2