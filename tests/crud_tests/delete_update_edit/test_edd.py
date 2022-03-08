import allure
import pytest

from locators.locators import StudentsPageLocators, CreatePageLocators
from pages.uitestpractice.create_page import CreatePage
from pages.uitestpractice.students_page import StudentsPage


@pytest.mark.usefixtures("setup")
class TestEdd:
    @allure.title("Validate details page opens")
    def test_details_can_open(self):
        students_page = StudentsPage(self.driver)
        students_page.open()
        assert students_page.get_table_rows() > 2
        students_page.click_element(*StudentsPageLocators.DETAILS_FIRST_USER)
        assert "details" in students_page.get_url().casefold()

    @allure.title("Validate edit page opens")
    def test_edit_can_open(self):
        students_page = StudentsPage(self.driver)
        students_page.open()
        assert students_page.get_table_rows() > 2
        students_page.click_element(*StudentsPageLocators.EDIT_FIRST_USER)
        assert "edit" in students_page.get_url().casefold()

    @allure.title("Validate delete page opens")
    def test_del_can_open(self):
        students_page = StudentsPage(self.driver)
        students_page.open()
        assert students_page.get_table_rows() > 2
        students_page.click_element(*StudentsPageLocators.DELETE_FIRST_USER)
        assert "delete" in students_page.get_url().casefold()
