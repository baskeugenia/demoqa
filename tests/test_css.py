import time
from pages.text_box_page import TextBoxPage

def test_text_box_submit(browser):
    tbp = TextBoxPage(browser)
    tbp.visit()
    assert tbp.btn_submit.check_css('color', 'rgba(255, 255, 255, 1)')
    assert tbp.btn_submit.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert tbp.btn_submit.check_css('borderColor', 'rgb(0, 123, 255)')