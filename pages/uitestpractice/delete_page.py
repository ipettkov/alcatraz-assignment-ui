from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from base.base_page import BasePage
from locators.locators import StudentsPageLocators, IframeAdLocators, CreatePageLocators, DeletePageLocators
from selenium.webdriver.support import expected_conditions as EC


class DeletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def delete(self):
        super().wait_for_element(*DeletePageLocators.DELETE_BTN)
        super().click_element(*DeletePageLocators.DELETE_BTN)
        return None