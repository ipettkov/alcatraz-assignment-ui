from selenium.webdriver.common.by import By


class NavigationPageLocators:
    HOME_MENU = (
        By.XPATH,
        "//div[@class='container']/descendant::a[@href='/Students/Index'][@class='navbar-brand']"
    )


class StudentsPageLocators:
    SEARCH_INPUT = (By.ID, "Search_Data")
    CREATE_STUDENT_BTN = (By.CSS_SELECTOR, "a[href='/Students/Create']")
    LAST_PAGE_LOCATOR = (By.CSS_SELECTOR, "li[class='PagedList-skipToLast'] > a")
    FIRST_PAGE_LOCATOR = (By.CSS_SELECTOR, "li[class='PagedList-skipToFirst'] > a")
    FIND_BTN = (By.CSS_SELECTOR, "div.input-group input[value='Find']")
    TABLE_ROWS = (By.XPATH, "//table//tr")
    DETAILS_FIRST_USER = (By.XPATH, "//table[@class='table']//tbody//tr[2]//td[4]//button[2]")
    EDIT_FIRST_USER = (By.XPATH, "//table[@class='table']//tbody//tr[2]//td[4]//button[1]")
    DELETE_FIRST_USER = (By.XPATH, "//table[@class='table']//tbody//tr[2]//td[4]//button[3]")


class CreatePageLocators:
    FIRST_NAME_FIELD = (By.ID, "FirstName")
    LAST_NAME_FIELD = (By.ID, "LastName")
    ENROLL_DATE = (By.ID, "EnrollmentDate")
    CREATE_BTN = (By.XPATH, "//input[@class='btn btn-default'][@value='Create']")
    DATE_VALID_ERR = (By.CSS_SELECTOR,
                      "span.field-validation-error.text-danger span[for='EnrollmentDate']")


class IframeAdLocators:
    IFRAME_ID = "ad_iframe"
    DISMISS_BUTTON = (By.ID, "dismiss-button")


class DeletePageLocators:
    DELETE_BTN = (By.CSS_SELECTOR, "input[type='submit'][value='Delete']")
