from selenium.webdriver.common.by import By

from managers.DriverManager import DriverManager


class TestPage:
    scroll_down_element_list = DriverManager \
        .get_driver().find_elements(By.XPATH,
                                    "//li[contains(@class, 'with-child')and not(contains(@class, 'active-path'))]")

    def get_elements_list(self):
        return self.scroll_down_element_list
