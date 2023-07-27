from selenium.webdriver import ActionChains
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
from elements.input import Input
from managers.DriverManager import DriverManager


class TimerPage:
    __timer = Element(By.XPATH, "//div[@class='timer timer--white timer--center']", "timer_element")
    __password_field = Input(By.XPATH, "//input[@placeholder='Choose Password']", "password_field")
    __email_field = Input(By.XPATH, "//input[@placeholder='Your email']", "email_field")
    __domain_field = Input(By.XPATH, "//input[@placeholder='Domain']", "domain_field")
    __dropdown = Button(By.XPATH, "//div[@class='dropdown__field']", "dropdown_button")
    __email_finish = Button(By.XPATH, "//div[normalize-space()='.com']", "email_finish")
    __checkbox = Button(By.XPATH, "//span[@class='icon icon-check checkbox__check']", "terms_button")
    __next_button = Button(By.XPATH, "//a[normalize-space()='Next']", "next_button")
    __avatar_box = Element(By.XPATH, "//div[@class='avatar-and-interests__avatar-box']", "avatar_box")

    def get_text_from_timer(self):
        return self.__timer.get_text()

    def fill_password(self, value):
        return self.__password_field.clear_and_fill(value)

    def fill_email(self, value):
        return self.__email_field.clear_and_fill(value)

    def fill_domain(self, value):
        return self.__domain_field.clear_and_fill(value)

    def click_dropdown(self):
        return self.__dropdown.click()

    def click_email_finish(self):
        return self.__email_finish.click()

    def click_checkbox(self):
        return self.__checkbox.click()

    def click_next_button(self):
        return self.__next_button.click()

    def avatar_box_is_displayed(self):
        return self.__avatar_box.is_visible()
