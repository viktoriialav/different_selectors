import pytest
from selene import browser

import config

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    driver_options = config.settings.driver_options

    browser.config.base_url = config.settings.base_url
    browser.config.window_width = config.settings.window_width
    browser.config.height = config.settings.window_height

    browser.config.driver_options = driver_options

    yield

    browser.quit()