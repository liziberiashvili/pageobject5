from selenium.webdriver.common.by import By

from managers.DriverManager import DriverManager


class DriverUtils:

    @staticmethod
    def find_element(xpath):
        return DriverManager.get_driver().find_element(By.XPATH, xpath)