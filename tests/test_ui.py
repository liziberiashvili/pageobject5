import pytest

from managers.DriverManager import DriverManager
from pages.TestPage import TestPage


@pytest.mark.usefixtures("setUp")
class TestUI:

    def test_scroll_down_menu(self):
        test_page = TestPage()
        print(test_page.getText())
