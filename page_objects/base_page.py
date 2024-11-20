from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        self._driver.get(url)

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _clear_text(self, locator: tuple, time: int = 10):
        self._wait_element_is_visible(locator, time)
        self._find(locator).clear()

    def _wait_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator), "Element is not visible")


    def _click(self, locator: tuple, time: int = 10):
        self._wait_element_is_visible(locator, time)
        self._find(locator).click()

    def current_url(self) -> str:
        return self._driver.current_url

    def _element_is_displayed(self, locator: tuple) -> bool:
        self._wait_element_is_visible(locator)
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _wait_element_is_not_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.invisibility_of_element(locator), "Element is visible")

    def _wait_element_is_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator), "Element is not clickable")

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_element_is_visible(locator, time)
        return self._find(locator).text

    def _get_attribute(self, locator: tuple, attribute_name: str) -> str:
        return self._find(locator).get_attribute(attribute_name)



