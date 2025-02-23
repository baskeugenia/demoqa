import time
from pages.text_box_page import TextBoxPage

def test_text_box(browser):
    tbp = TextBoxPage(browser)
    tbp.visit()
    un = 'SOMENAME'
    tbp.user_name.send_keys(un)
    ca = 'SOMEADDRESS'
    tbp.current_address.send_keys(ca)
    time.sleep(2)
    tbp.btn_submit.click_force()
    time.sleep(2)
    outun = tbp.output_name.get_text()
    outca = tbp.output_current_address.get_text()
    time.sleep(2)
    
    assert outun == 'Name:' + un
    assert outca == 'Current Address :' + ca