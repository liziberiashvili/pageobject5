from selenium.webdriver.common.by import By

from elements.button import Button
from utils.DriverUtils import DriverUtils


class DynamicPropertiesPage:
    __enable_button = Button("//button[@id='enableAfter']", "enable_button")
    __color_changeable_button = Button("//button[@id='colorChange']", "color_change_button")
    __visible_after_button = Button("//button[@id='visibleAfter']", "visible_after_button")

    def wait_for_enable_button(self):
         DriverUtils.wait_for_element_enable(self.__enable_button.find_element())

    def wait_for_color_changeable_button(self):
        locator = By.XPATH, self.__color_changeable_button.locator
        attribute = "class"
        text = "mt-4 text-danger btn btn-primary"
        DriverUtils.wait_for_color_change(locator, attribute, text)

    def wait_for_visible_button(self):
        locator = By.XPATH, self.__visible_after_button.locator
        DriverUtils.wait_for_visible(locator)



