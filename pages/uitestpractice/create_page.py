from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from locators.locators import CreatePageLocators

import allure


class CreatePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Adding user with first name: {0}, last name: {1}, date: {2}")
    def create_user(self, first_name, last_name, date):
        self.type(*CreatePageLocators.FIRST_NAME_FIELD, text=first_name)
        self.type(*CreatePageLocators.LAST_NAME_FIELD, text=last_name)
        self.type(*CreatePageLocators.ENROLL_DATE, text=date)
        try:
            self.click_element(*CreatePageLocators.CREATE_BTN)
        except StaleElementReferenceException:
            pass

    @allure.step("Input {} in date field")
    def input_date(self, date):
        self.type(*CreatePageLocators.ENROLL_DATE, text=date)
        self.retry_click(*CreatePageLocators.CREATE_BTN)
