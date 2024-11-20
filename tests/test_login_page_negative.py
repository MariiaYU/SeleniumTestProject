import pytest
from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_text",
                             [("incorrect", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_text):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.error_text() == expected_error_text, "Error message is not expected"
