import time
from pages.progress_bar_page import ProgressBarPage
from selenium.webdriver.common.keys import Keys


def test_progress_bar(browser):
    pbp = ProgressBarPage(browser)
    pbp.visit()

    pbp.btn_start_stop.click()

    assert pbp

    while True:
        if pbp.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            print(pbp.progress_bar.get_text())
            pbp.btn_start_stop.click()
            break;


    assert pbp.progress_bar.get_text() == '51%'


