import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from locators.locators import StudentsPageLocators


class StudentsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to(self, location: str):
        if location.casefold() == "create":
            self.retry_click(*StudentsPageLocators.CREATE_STUDENT_BTN)
            self.dismiss_ad()
        elif location.casefold() == "last page":
            self.retry_click(*StudentsPageLocators.LAST_PAGE_LOCATOR)
        elif location.casefold() == "first page":
            self.retry_click(*StudentsPageLocators.FIRST_PAGE_LOCATOR)

        return None

    def get_table_rows(self):
        self.wait_for_elements(*StudentsPageLocators.TABLE_ROWS, wait=5)
        return len(self.driver.find_elements(*StudentsPageLocators.TABLE_ROWS))

    def table_is_empty(self):
        try:
            self.wait_for_elements(*StudentsPageLocators.TABLE_ROWS, wait=2)
            return True
        except TimeoutException:
            return False

    @allure.step("Finding user {0} in table")
    def find_user_in_table(self, name: str):
        """
        Finds user by his first or last name. Method will work with
        both with first and last name and will return the element with the searched name
        Method is case-sensitive
        :param name: str
        :return: WebElement of the container in which first or last name is
        """
        return self.driver.find_element(By.XPATH, f"//table[@class='table']/descendant::td[contains(text(), '{name}')]")

    @allure.step("Clicking {1} on user {0}")
    def action_on_user(self, name: str, action: str):
        """
        Clicks EDIT, UPDATE, DELETE on specific user
        name is case-sensitive
        action is case-insensitive
        :param name: str
        :param action: str
        :return:
        """
        dynamic_locator = (By.XPATH, f"//table[@class='table']/descendant::td[contains(text(), '{name}')]/parent::tr/descendant::button[contains(text(), '{action.upper()}')]")
        self.wait_for_element(*dynamic_locator)
        self.retry_click(*dynamic_locator)

        return None






    # def create_student(self):
    #     self.driver.find_element(*StudentsPageLocators.CREATE_STUDENT_BTN).click()
    #     super().dismiss_ad()
    #     self.driver.find_element(*CreatePageLocators.FIRST_NAME_FIELD).send_keys("Hi, can I make it?")

    # def _dismiss_ad(self):
    #     self.driver.switch_to.frame("aswift_2")
    #     iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
    #
    #     dismiss_btn = "dismiss-button"
    #     for iframe in iframes:
    #         self.driver.switch_to.frame(iframe)
    #         try:
    #             WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.ID, dismiss_btn)))
    #             self.driver.find_element(By.ID, dismiss_btn).click()
    #         except NoSuchElementException:
    #             pass
    #         except StaleElementReferenceException:
    #             pass
    #
    #     self.driver.switch_to.default_content()





