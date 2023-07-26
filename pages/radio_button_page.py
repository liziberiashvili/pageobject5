from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element


class RadioButtonPage:
    __radio_button = "//label[normalize-space()='{}']"
    __text = Element(By.XPATH, "//span[@class='text-success']", "text")

    def click_radio_button(self, value):
        radio_button = Button(By.XPATH, self.__radio_button.format(value), "radio_button")
        radio_button.click()

    def get_text(self):
        return self.__text.get_text()
