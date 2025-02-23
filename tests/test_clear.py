import time
from pages.text_box_page import TextBoxPage

def test_clear(browser):
    tbp = TextBoxPage(browser)
    tbp.visit()
    tbp.user_name.send_keys('My Name')
    time.sleep(2)
    print('*'*100,tbp.user_name.get_text())
    tbp.user_name.clear()
    time.sleep(2)
    print('*'*100,tbp.user_name.get_text())
    assert tbp.user_name.get_text() == ''