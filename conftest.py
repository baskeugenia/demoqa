import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    #driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()

    binary_yandex_driver_file = './yandexdriver.exe'  # path to YandexDriver

    service = webdriver.chrome.service.Service(executable_path=binary_yandex_driver_file)  # v4.10+
    # service = webdriver.ChromeService(executable_path=binary_yandex_driver_file) #v4.11+

    driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()