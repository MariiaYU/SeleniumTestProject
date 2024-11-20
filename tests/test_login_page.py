import pytest
from page_objects.login_page import LoginPage
from page_objects.login_success_page import SuccessLogin


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        login_success_page = SuccessLogin(driver)
        login_page.open()
        login_page.execute_login("student", "Password123")
        assert login_success_page.expected_url == login_success_page.current_url(), "The url is not expected one"
        assert login_success_page.success_text == "Logged In Successfully", "Congratulation text is not expected"
        assert login_success_page.logout_button_is_displayed(), "Logout button is not displayed"


