import time
from pages.form_page import FormPage


def test_login_form(browser):
    fp = FormPage(browser)
    fp.visit()

    assert not fp.modal_dialog.exist()

    time.sleep(2)
    fp.first_name.send_keys('Firstname')
    fp.last_name.send_keys('Lastname')
    fp.user_email.send_keys('smth@xxx.com')
    fp.gender_radio.click_force()
    fp.user_number.send_keys('9876543210')
    fp.hobbies.click_force()
    fp.current_address.send_keys('Some address')
    time.sleep(2)
    fp.btn_submit.click_force()
    time.sleep(2)

    assert fp.modal_dialog.exist()
    fp.modal_dialog.click_force()
    time.sleep(2)

def test_state_city(browser):
    fp = FormPage(browser)
    fp.visit()