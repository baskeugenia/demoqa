from pages.demoqa import DemoQa


def test_title(browser):
    demoqa = DemoQa(browser)
    demoqa.visit()
    print(demoqa.get_title())
    assert not demoqa.get_title() == None