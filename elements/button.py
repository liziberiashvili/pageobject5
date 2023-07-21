from elements.element import Element


class Button(Element):
    def __init__(self, locator, name):
        super().__init__(locator, name)