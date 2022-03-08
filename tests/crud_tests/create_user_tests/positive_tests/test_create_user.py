import allure
import pytest

from locators.locators import StudentsPageLocators
from pages.uitestpractice.create_page import CreatePage
from pages.uitestpractice.delete_page import DeletePage
from pages.uitestpractice.students_page import StudentsPage
from utils.functions import generate_random_name, get_curr_date

CREATE = "create"
DELETE = "delete"


@pytest.mark.usefixtures("setup")
class TestCreateUser:
    # ideally I would check db, api, and assert some confirmation from
    # app which is missing here. Only thing I can do is to assert that I'm back at home page
    @allure.title("Create user valid user")
    @allure.description("Create user and validate creation by finding user")
    def test_create_valid_user(self):
        students_page = StudentsPage(self.driver)
        students_page.open()
        students_page.navigate_to(CREATE)
        create_page = CreatePage(self.driver)
        assert create_page.get_url().casefold()[-6::] == "create"

        first_name = generate_random_name("female", True)
        last_name = generate_random_name(False)
        date = get_curr_date()

        create_page.create_user(first_name, last_name, date)
        assert students_page.get_url().casefold()[-5::] == "index"

        students_page.type(*StudentsPageLocators.SEARCH_INPUT, text=first_name)
        students_page.click_element(*StudentsPageLocators.FIND_BTN)
        assert students_page.find_user_in_table(first_name).text == first_name

        students_page.action_on_user(last_name, DELETE)
        delete_page = DeletePage(self.driver)
        delete_page.delete()

    @allure.title("Validate create input fields")
    @allure.description("Test fields validation")
    @pytest.mark.parametrize('param1, param2, expected_url',
                             [
                                 ('', 'last', "create"),
                                 ('first', '', 'create'),
                                 ('', '', 'create')
                             ]
                             )
    def test_create_fields(self, param1, param2, expected_url):
        students_page = StudentsPage(self.driver)
        students_page.open()
        students_page.navigate_to(CREATE)
        create_page = CreatePage(self.driver)
        date = get_curr_date()
        create_page.create_user(param1, param2, date)
        # looking for create page param in link as it should not allow user to be created
        assert create_page.get_url().casefold()[-6::] == expected_url, "failed, user is created navigated to home page"

        # TODO refactor parameterization^ don't open browser each time
