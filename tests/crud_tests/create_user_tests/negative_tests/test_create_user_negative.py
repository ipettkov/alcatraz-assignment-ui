import allure
import pytest

from locators.locators import CreatePageLocators
from pages.uitestpractice.create_page import CreatePage
from pages.uitestpractice.students_page import StudentsPage
from utils.functions import get_curr_date


# @pytest.mark.usefixture("setup")
class TestCreateUserNegative:
    pass
# TODO  finish use after execution refactoring as with current setup browser will open 5 times
# @allure.title("Test input validation")
# @allure.description("Perform series of input that field shouldn't allow")
# @pytest.mark.parametrize('param, expected',
#                          [
#                              ('05:05:03', "EnrollmentDate"),
#                              ('02=04=22', "EnrollmentDate"),
#                              ('03|04|23', "EnrollmentDate"),
#                              ('10?31?22', "EnrollmentDate"),
#                              ('Today', "EnrollmentDate")
#                          ]
#                          )
# def test_validate_date_field(self, param, expected):
#     students_page = StudentsPage(self.driver)
#     students_page.open()
#     students_page.navigate_to("create")
#     create_page = CreatePage(self.driver)
#     create_page.input_date(param)
#     assert
