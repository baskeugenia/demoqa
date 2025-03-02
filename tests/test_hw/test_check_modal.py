from pages.modal_dialogs_page import ModalDialogsPage
import time


def test_check_modal(browser):
    mdp = ModalDialogsPage(browser)
    mdp.visit()

    print(mdp.get_title())

    # esli stranica nedostupna, title
    # budet kod oshibki - 404, ili 502, itd
    if mdp.get_title() == 'DEMOQA':
        mdp.btn_show_small.click()
        time.sleep(3)
        mdp.icon_close.click_force()
        time.sleep(3)

        assert not mdp.icon_close.exist()

        mdp.btn_show_large.click()
        time.sleep(3)
        mdp.icon_close.click_force()
        time.sleep(3)

        assert not mdp.icon_close.exist()



