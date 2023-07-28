from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
from elements.input import Input
from pages.base_form import BaseForm


class TimerPage2(BaseForm):
    __unselect_all_checkbox = Button(By.XPATH, "//label[@for='interest_unselectall']", "unselect_all")
    __interest_purple_checkbox = Button(By.XPATH, "//label[@for='interest_purple']", "purple")
    __interest_cotton_checkbox = Button(By.XPATH, "//label[@for='interest_cotton']", "cotton")
    __interest_drywall_checkbox = Button(By.XPATH, "//label[@for='interest_drywall']", "drywall")
    __upload_image_button = Input(By.XPATH, "//a[normalize-space()='upload']", "upload_image")
    __next_button = Button(By.XPATH, "//button[normalize-space()='Next']", "next_button")

    def __init__(self):
        super().__init__(By.XPATH, "unique element xpath", "unique element")

    def unselect_all_interest(self):
        return self.__unselect_all_checkbox.click()

    def check_purple_interest(self):
        return self.__interest_purple_checkbox.click()

    def check_cotton_interest(self):
        return self.__interest_cotton_checkbox.click()

    def check_drywall_interest(self):
        return self.__interest_drywall_checkbox.click()

    def find_upload_image_button(self):
        return self.__upload_image_button.click()

    def upload_profile_image(self, path):
        return self.__upload_image_button.upload_image(path)

    def press_enter(self):
        return self.__upload_image_button.press_enter()

    def click_next_button(self):
        return self.__next_button.click()
