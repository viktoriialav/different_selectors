from typing import Literal, Optional

from pydantic_settings import BaseSettings
from selenium.webdriver import ChromeOptions, FirefoxOptions

from diff_selectors.utils import path

DriverName = Literal['chrome', 'firefox']
EnvContext = Literal['local_litecart', 'local_demo', 'selenoid_demo']


class Settings(BaseSettings):
    context: str = 'local_litecart'

    base_url: str = 'https://litecart.stqa.ru/en'
    driver_name: str = 'chrome'
    window_width: int = 1920
    window_height: int = 1080

    @property
    def driver_options(self):
        if self.driver_name == 'chrome':
            options = ChromeOptions()
        else:
            options = FirefoxOptions()

        options.page_load_strategy = 'eager'

        return options

    @classmethod
    def in_context(cls, env: Optional[EnvContext] = None):
        env = env or cls().context
        return cls(_env_file=path.abs_path_from_root(f'.env.{env}'))


settings = Settings.in_context()
