from pages.koupPage import KoupPage
from pages.koupPageAdd import KoupPageAdd
import time


def test_koup_add(browser):
    kp = KoupPage(browser)
    kpa = KoupPageAdd(browser)

    kp.visit()
    time.sleep(3)

    assert kp.link_add.get_text() == 'Add/Remove Elements'

    kp.link_add.click()
    time.sleep(3)

    print(kpa.get_url())
    assert kpa.equal_url()

    assert kpa.btn_add.get_text() == 'Add Element'

    assert kpa.btn_add.get_dom_attribute('onclick') == 'addElement()'

    for i in range(4):
        kpa.btn_add.click()

    assert kpa.btns_delete.check_count_elements(4)

    for el in kpa.btns_delete.find_elements():
        assert el.text == 'Delete'

    while kpa.btns_delete.exist():
        kpa.btns_delete.click()

    assert not kpa.btns_delete.exist()