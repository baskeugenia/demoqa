import time
from pages.webtables_page import WebtablesPage
from selenium.webdriver.common.keys import Keys


def test_webtables_pagination(browser):
    wp = WebtablesPage(browser)
    wp.visit()

    wp.btn_select_size.click_force()
    time.sleep(2)
    wp.btn_select_size.send_keys(Keys.ARROW_UP)
    time.sleep(2)


    assert wp.btn_prev.get_dom_attribute('disabled')
    assert wp.btn_next.get_dom_attribute('disabled')

    for i in range(1,4):
        add_row(wp, i)

    time.sleep(2)

    assert wp.page_info.get_dom_attribute('value') == '1'
    assert wp.btn_prev.get_dom_attribute('disabled')
    assert not wp.btn_next.get_dom_attribute('disabled')

    wp.btn_next.click()
    time.sleep(2)

    assert wp.page_info.get_dom_attribute('value') == '2'
    assert not wp.btn_prev.get_dom_attribute('disabled')
    assert wp.btn_next.get_dom_attribute('disabled')

    wp.btn_prev.click()

    assert wp.page_info.get_dom_attribute('value') == '1'



def add_row(wp, i):

    wp.btn_add.click()
    time.sleep(2)

    assert wp.modal_form.exist()

    wp.first_name.send_keys('FIRSTNAME' + str(i))
    wp.last_name.send_keys('LASTNAME' + str(i))
    wp.user_email.send_keys(str(i) + 'email@exp.com')
    wp.age.send_keys('3' + str(i))
    wp.salary.send_keys('30003')
    wp.department.send_keys('Business')
    wp.btn_submit.click()
    time.sleep(2)

    assert not wp.modal_form.exist()


