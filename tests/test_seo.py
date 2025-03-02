from pages.demoqa import DemoQa
from pages.accordian_page import AccordianPage
from pages.alerts_page import AlertsPage
from pages.browser_tab_page import BrowserTabPage
import time
import pytest


def test_seo(browser):
    demoqa = DemoQa(browser)
    demoqa.visit()
    assert browser.title == 'DEMOQA'


@pytest.mark.parametrize('pages', [AccordianPage, AlertsPage, DemoQa, BrowserTabPage])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)

    assert page.get_title() == 'DEMOQA'


@pytest.mark.parametrize('pages', [AccordianPage, AlertsPage, DemoQa, BrowserTabPage])
def test_seo_meta(browser, pages):
    page = pages(browser)
    page.visit()
    assert page.viewport.exist()
    print('!'*100, page.viewport.get_dom_attribute('name'))
    print('!'*100, page.viewport.get_dom_attribute('content'))