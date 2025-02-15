from pages.modal_dialogs_page import ModalDialogsPage
import time


def test_modal_elements(browser):
    mdp = ModalDialogsPage(browser)
    mdp.visit()
    time.sleep(3)

    assert mdp.btns_submenu.check_count_elements(5)


def test_navigation_modal(browser):
    mdp = ModalDialogsPage(browser)
    mdp.visit()
    mdp.refresh()
    time.sleep(3)
    mdp.icon.click()
    time.sleep(3)
    mdp.back()
    time.sleep(3)
    browser.set_window_size(900, 400)
    mdp.forward()
    assert mdp.get_url() == 'https://demoqa.com/'
    assert mdp.get_title() == 'DEMOQA'
    browser.set_window_size(1000, 1000)
    time.sleep(3)
