from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from base.base_page import BasePage
from locators.locators import StudentsPageLocators, IframeAdLocators, CreatePageLocators
from selenium.webdriver.support import expected_conditions as EC


class EditPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
