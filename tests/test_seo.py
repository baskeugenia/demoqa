from pages.demoqa import DemoQa


def test_seo(browser):
    demoqa = DemoQa(browser)
    demoqa.visit()
    assert browser.title == 'DEMOQA'
