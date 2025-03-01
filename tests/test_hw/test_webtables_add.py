import time
from pages.webtables_page import WebtablesPage
from selenium.webdriver.common.keys import Keys


def test_webtables_add(browser):
    wp = WebtablesPage(browser)
    wp.visit()

    assert not wp.modal_form.exist()

    wp.btn_add.click()
    time.sleep(2)
    wp.btn_submit.click()
    time.sleep(2)

    assert wp.modal_form.exist()

    wp.first_name.send_keys('FIRSTNAME')
    wp.last_name.send_keys('LASTNAME')
    wp.user_email.send_keys('email@exp.com')
    wp.age.send_keys('33')
    wp.salary.send_keys('30003')
    wp.department.send_keys('Business')
    wp.btn_submit.click()
    time.sleep(2)

    assert not wp.modal_form.exist()

    wp.btn_edit_4.click()
    time.sleep(2)
    new_name = 'NEWNAME'
    wp.first_name.send_keys(Keys.CONTROL+'a')
    wp.first_name.send_keys(Keys.DELETE)
    wp.first_name.send_keys(new_name)
    time.sleep(2)
    wp.btn_submit.click()
    time.sleep(2)

    assert wp.cell_first_name_4.get_text() == new_name

    wp.btn_delete_4.click()
    assert wp.cell_first_name_4.get_text() == ' '

