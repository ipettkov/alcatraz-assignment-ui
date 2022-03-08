from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from extension.webdriver_extended import WebDriverExtended
from helpers.webdriver_listener import WebDriverListener


class DriverFactory:
    @staticmethod
    def get_driver(config) -> WebDriverExtended:
        if config["browser"] == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            if config["headless_mode"] is True:
                options.add_argument("--headless")
            driver = WebDriverExtended(
                webdriver.Chrome(ChromeDriverManager().install(), options=options),
                WebDriverListener(), config
            )
            return driver
        elif config["browser"] == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            if config["headless_mode"] is True:
                options.headless = True
            driver = WebDriverExtended(
                webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options),
                WebDriverListener(), config
            )
            return driver
