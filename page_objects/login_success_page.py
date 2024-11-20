import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec

from page_objects.base_page import BasePage


class SuccessLogin(BasePage):
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __congratulation_text = (By.XPATH, "//h1[@class='post-title']")
    __logout_button = (By.XPATH, "//a[@class='wp-block-button__link has-text-color has-background has-very-dark-gray-background-color']")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)


    @property
    def expected_url(self) -> str:
        return self.__url

    @property
    def success_text(self) -> str:
        return super()._get_text(self.__congratulation_text)


    def logout_button_is_displayed(self) -> bool:
        return super()._element_is_displayed(self.__logout_button)




