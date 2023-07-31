from selenium.webdriver import ActionChains

from elements.element import Element


class Slider(Element):
    def __init__(self, by, locator, name):
        super().__init__(by, locator, name)


