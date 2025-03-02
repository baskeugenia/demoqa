import pytest

from pages.demoqa import DemoQa
from pages.radio_button_page import RadioButtonPage
import time


@pytest.mark.skip
def test_decor(browser):
    page = DemoQa(browser)
    page.visit()
    time.sleep(2)

    assert page.h5.check_count_elements(6)

    for el in page.h5.find_elements():
        assert not el.text == ''


@pytest.mark.skipif(True, reason="some reason")
def test_decor_1(browser):
    page = RadioButtonPage(browser)
    page.visit()
    time.sleep(2)

    page.inp_yes.click_force()
    assert page.text_out.get_text() == 'Yes'

    page.inp_imp.click_force()
    assert page.text_out.get_text() == 'Impressive'

    assert page.inp_no.get_dom_attribute('disabled')