from selenium.webdriver.common.by import By

from elements.BaseElement import BaseElement


class TestPage:
    text_element = BaseElement("//a[@id='m-documentation']", "saxeli")

    def getText(self):
        return self.text_element.get_text()
