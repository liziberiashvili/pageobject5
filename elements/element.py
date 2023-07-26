from selenium.webdriver.common.by import By

from managers.DriverManager import DriverManager


class Element:

    def __init__(self, locator, name):
        self.locator = locator
        self.name = name

    def find_element(self):
        return DriverManager.get_driver().find_element(By.XPATH, self.locator)

    def find_elements(self):
        return DriverManager.get_driver().find_elements(By.XPATH, self.locator)

    def is_visible(self):
        return DriverManager.get_driver().find_element(By.XPATH, self.locator).is_displayed()

    def is_exists(self):
        if len(DriverManager.get_driver().find_elements(By.XPATH, self.locator)) > 0:
            return True
        else:
            return False

    def click(self):
        DriverManager.get_driver().find_element(By.XPATH, self.locator).click()

    def get_text(self):
        return DriverManager.get_driver().find_element(By.XPATH, self.locator).text

    def get_text_from_attribute(self, name):
        return DriverManager.get_driver().find_element(By.XPATH, self.locator).get_attribute(name)

    def is_enabled(self):
        return DriverManager.get_driver().find_element(By.XPATH, self.locator).is_enabled()

    def clear(self):
        return DriverManager.get_driver().find_element(By.XPATH, self.locator).clear()
