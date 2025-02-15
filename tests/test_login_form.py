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
    fp.gender_radio.click()
    fp.user_number.send_keys('987654321')
    time.sleep(2)
    fp.btn_submit.click()
    time.sleep(2)