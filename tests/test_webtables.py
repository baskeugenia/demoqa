import time
from pages.webtables_page import WebtablesPage

def test_text_box_submit(browser):
    wp = WebtablesPage(browser)
    wp.visit()

    assert not wp.no_data.exist()
