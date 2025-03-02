import time
from pages.slider_page import SliderPage
from selenium.webdriver.common.keys import Keys


def test_slider(browser):
    sp = SliderPage(browser)
    sp.visit()

    assert sp.slider_value.exist()
    assert sp.slider_input.exist()

    while not sp.slider_value.get_dom_attribute('value') == '50':
        sp.slider_input.send_keys(Keys.ARROW_RIGHT)

    time.sleep(2)

    assert sp.slider_value.get_dom_attribute('value') == '50'





