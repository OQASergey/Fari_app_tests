import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='module', autouse=True)
def browser_conditions():
    browser.config.driver_name = 'chrome'
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://fari.app'

    browser.open()
    print('')
    print('')
    print('[ Параметры тестов ]')
    print('Браузер - Chrome')
    print('Размер окна - По умолчанию')
    print('Путь до скриншотов = C:/_test_screenshots/Fery_app_tests/')
    print('')
    print('**Начало исполнения тестового набора**')

    yield

    browser.quit()
    print('')
    print('**Завершение исполнения тестового набора**')
    print('Путь до скриншотов = C:/_test_screenshots/Fery_app_tests/')