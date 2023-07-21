from elements.element import Element


class TextField(Element):

    def __init__(self, locator, name):
        super().__init__(locator, name)