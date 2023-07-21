from selenium.webdriver.common.by import By

from elements.element import Element
from managers.DriverManager import DriverManager


class Input(Element):
    def __init__(self, locator, name):
        super().__init__(locator, name)

    def send_text(self, value):
        return DriverManager.get_driver().find_element(By.XPATH, self.locator).send_keys(value)