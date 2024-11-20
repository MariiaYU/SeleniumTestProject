from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class Exceptions(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button = (By.XPATH, "//button[@id='add_btn']")
    __row1_input = (By.XPATH, "//div[@id='row1']/input")
    __row2_input = (By.XPATH,"//div[@id='row2']/input")
    __save_button_row1 = (By.XPATH, "//div[@id='row1']/button[@id='save_btn']")
    __save_button_row2 = (By.XPATH, "//div[@id='row2']/button[@id='save_btn']")
    __edit_button_row1 = (By.XPATH, "//div[@id='row1']/button[@id='edit_btn']")
    __save_confirmation_text = (By.XPATH, "//div[@id='confirmation']")
    __attribute_name_for_message = "value"
    __instruction_text = (By.XPATH, "//p[@id='instructions']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def add_new_row(self):
        super()._click(self.__add_button)
        super()._wait_element_is_visible(self.__row2_input)

    def add_second_food(self, food_name: str):
        super()._type(self.__row2_input, food_name)
        super()._click(self.__save_button_row2)
        super()._wait_element_is_visible(self.__save_confirmation_text)

    def is_row2_displayed(self) -> bool:
        return super()._element_is_displayed(self.__row2_input)

    def get_confirmation_text(self) -> str:
        return super()._get_text(self.__save_confirmation_text)

    def edit_row1(self, food_name: str):
        super()._click(self.__edit_button_row1)
        super()._wait_element_is_clickable(self.__row1_input)
        super()._clear_text(self.__row1_input)
        super()._type(self.__row1_input, food_name)
        super()._click(self.__save_button_row1)

    def get_row1_text(self) -> str:
        return super()._get_attribute(self.__row1_input, self.__attribute_name_for_message)

    def get_instruction_text(self) -> str:
        return super()._get_text(self.__instruction_text)

    def check_instruction_text(self) -> bool:
        return super()._wait_element_is_not_visible(self.__instruction_text)
