import pytest
from selenium.webdriver.common.by import By

from managers.DriverManager import DriverManager
from pages.TestPage import TestPage


@pytest.mark.usefixtures("setUp")
class TestUI:

    def test_scroll_down_menu(self):
        test_page = TestPage()
        scroll_down_element_list = test_page.get_elements_list()
        assert scroll_down_element_list[0].text == "Overview"
