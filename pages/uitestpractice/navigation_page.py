from base.base_page import BasePage
from locators.locators import NavigationPageLocators

import allure


class NavigationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


