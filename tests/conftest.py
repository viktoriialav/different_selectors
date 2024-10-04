import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

import config


@pytest.fixture(scope='function')
def browser_management_selene():
    driver_options = config.settings.driver_options

    browser.config.base_url = config.settings.base_url
    browser.config.window_width = config.settings.window_width
    browser.config.height = config.settings.window_height

    browser.config.driver_options = driver_options

    yield

    browser.quit()


@pytest.fixture(scope='function')
def browser_management_selenium():
    driver_options = config.settings.driver_options

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                              options=driver_options)
    driver.set_window_size(width=config.settings.window_width,
                           height=config.settings.window_height)

    yield driver

    driver.quit()
