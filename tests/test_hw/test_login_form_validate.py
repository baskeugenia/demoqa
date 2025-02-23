import time
from pages.form_page import FormPage

def test_login_form_validate(browser):
    fp = FormPage(browser)
    fp.visit()

    plhldr = fp.first_name.get_dom_attribute('placeholder')
    assert plhldr == 'First Name'

    plhldr = fp.last_name.get_dom_attribute('placeholder')
    assert plhldr == 'Last Name'

    plhldr = fp.user_email.get_dom_attribute('placeholder')
    assert plhldr == 'name@example.com'

    pattern = fp.user_email.get_dom_attribute('pattern')
    assert pattern == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    assert fp.form.get_dom_attribute('class') is not 'was validated'

    fp.btn_submit.click_force()
    assert fp.form.get_dom_attribute('class') == 'was-validated'

    time.sleep(2)

    assert not fp.modal_dialog.exist()