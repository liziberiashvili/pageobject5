
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from managers.DriverManager import DriverManager


class DriverUtils:

    @staticmethod
    def find_element(xpath):
        return DriverManager.get_driver().find_element(By.XPATH, xpath)

    @staticmethod
    def wait_for_element_enable(element):
        WebDriverWait(DriverManager.get_driver(), timeout=15)\
            .until(expected_conditions.element_to_be_clickable(element))

    @staticmethod
    def wait_for_color_change(locator, attribute, text):
        WebDriverWait(DriverManager.get_driver(), timeout=15)\
            .until(expected_conditions.text_to_be_present_in_element_attribute(locator, attribute, text))

    @staticmethod
    def wait_for_visible(locator):
        WebDriverWait(DriverManager.get_driver(), timeout=15)\
            .until(expected_conditions.visibility_of_element_located(locator))