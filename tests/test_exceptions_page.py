import pytest
from page_objects.exceptions_page import Exceptions


class TestExceptionsScenarios:
    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_no_element_error(self, driver):
        exception_page = Exceptions(driver)
        exception_page.open()
        exception_page.add_new_row()
        assert exception_page.is_row2_displayed(), "Row 2 should be displayed, but it's not"


    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_element_not_interactable(self, driver):
        exception_page = Exceptions(driver)
        exception_page.open()
        exception_page.add_new_row()
        exception_page.add_second_food("Sushi")
        assert exception_page.get_confirmation_text() == "Row 2 was saved", "Confirmation message is not expected"


    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        exception_page = Exceptions(driver)
        exception_page.open()
        exception_page.edit_row1("Sushi")
        assert exception_page.get_row1_text() == "Sushi", "The text wasn't changed"
        assert exception_page.get_confirmation_text() == "Row 1 was saved", "Confirmation message is not expected"


    @pytest.mark.exceptions
    #@pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        exception_page = Exceptions(driver)
        exception_page.open()
        assert exception_page.get_instruction_text() == "Push “Add” button to add another row", "Text is not expected one"
        exception_page.add_new_row()
        assert not exception_page.check_instruction_text(), "Text is still displayed, but should not"



