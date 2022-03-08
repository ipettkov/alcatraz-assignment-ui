import allure
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Opening main page")
    def open(self):
        self.driver.open()

    @allure.step("Dismissing google ad")
    def dismiss_ad(self):
        try:
            WebDriverWait(self.driver, 1).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "aswift_2")))
            self.driver.find_element(By.ID, "dismiss-button").click()

            WebDriverWait(self.driver, 1).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ad_iframe")))
            WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.ID, "dismiss-button")))
            self.retry_click(By.ID, "dismiss-button")
        except NoSuchElementException:
            WebDriverWait(self.driver, 1).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ad_iframe")))
            WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.ID, "dismiss-button")))
            self.retry_click(By.ID, "dismiss-button")
            # self.driver.find_element(By.ID, "dismiss-button")
            # pass
            # WebDriverWait(self.driver, 1).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ad_iframe")))
            # WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.ID, "dismiss-button")))
            # self.driver.find_element(By.ID, "dismiss-button").click()
        except TimeoutException:
            pass
        except StaleElementReferenceException:
            pass
        finally:
            pass


            #
            # WebDriverWait(self.driver, 1).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ad_iframe")))
            # self.driver.find_element(By.ID, "dismiss-button").click()
            # self.driver.find_element(By.XPATH,
            #                          "//div[@id='large-banner-rda-vanilla']/descendant::div[@id='dismiss-button']").click()
        # except StaleElementReferenceException:
        #     pass
            # WebDriverWait(self.driver, 1).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ad_iframe")))
            # self.driver.find_element(By.ID, "dismiss-button").click()

        # except TimeoutException:
        #     WebDriverWait(self.driver, 1).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ad_iframe")))
        #     self.driver.find_element(By.ID, "dismiss-button").click()

        # iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
        #
        # dismiss_btn = "dismiss-button"
        # for iframe in iframes:
        #     self.driver.switch_to.frame(iframe)
        #     try:
        #         WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.ID, dismiss_btn)))
        #         self.retry_click(By.ID, dismiss_btn)
        #     except NoSuchElementException:
        #         pass
        #     except StaleElementReferenceException:
        #         pass

        self.driver.switch_to.default_content()

    @allure.step("Clicking on {0}")
    def click_element(self, *locator):
        self.wait_for_element(*locator)
        self.retry_click(*locator)
        return None

    @allure.step("Typing {1}")
    def type(self, *locator, text=None):
        self.wait_for_element(*locator)
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)
        return None

    def get_element(self, *locator):
        self.wait_for_element(*locator)
        return self.driver.find_element(*locator)

    def get_elements(self, *locator):
        self.wait_for_elements(*locator)
        return self.driver.find_elements(*locator)

    def get_text(self, *locator):
        self.wait_for_element(*locator)
        return self.driver.find_element(*locator).text.strip()

    def get_url(self):
        return self.driver.current_url

    @allure.step("Waiting for element with locator {0} to be present")
    def wait_for_element(self, *locator, wait=5):
        by, loc = locator
        WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((by, loc)))
        return None

    @allure.step("Waiting for elements with {0} locator to be present")
    def wait_for_elements(self, *locator, wait=5):
        by, loc = locator
        WebDriverWait(self.driver, wait).until(EC.presence_of_all_elements_located((by, loc)))
        return None

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
        try:
            self.driver.find_element(
                By.XPATH,
                f"//table[@class='table']/descendant::td[contains(text(), '{name}')]/parent::tr/descendant::button[contains(text(), '{action.upper()}')]").click()
        except StaleElementReferenceException:
            pass

    def retry_click(self, *locator):
        result = False
        attempts = 0

        while attempts < 2:
            try:
                self.driver.find_element(*locator).click()
                result = True
            except StaleElementReferenceException:
                attempts += 1
            return result
