import time
from pages.text_box_page import TextBoxPage

def test_placeholder(browser):
    tbp = TextBoxPage(browser)
    tbp.visit()
    plhldr = tbp.user_name.get_dom_attribute('placeholder')
    time.sleep(2)
    print('*'*100, plhldr)
    assert plhldr == 'Full Name'