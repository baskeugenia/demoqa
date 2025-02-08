from pages.demoqa import DemoQa
import time


def test_check_icon(browser):
    demoqa_page = DemoQa(browser)
    demoqa_page.visit()
    time.sleep(3)
    demoqa_page.icon.click()
    time.sleep(3)
    assert demoqa_page.equal_url()
    assert demoqa_page.icon.exist()
