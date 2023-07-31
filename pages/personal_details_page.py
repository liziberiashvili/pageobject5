from selenium.webdriver.common.by import By

from elements.button import Button

from elements.input import Input
from elements.slider import Slider


class PersonalDetailsPage:
    __first_name = Input(By.XPATH, "//div[contains(text(),'First name')]/following-sibling::div", "saxeli")
    __title = Button(By.XPATH, "//div[contains(text(),'Title')]/following-sibling::div", "title")
    __mr = Button(By.XPATH, "//div[normalize-space()='Mr']", "kaci")
    __surname = Input(By.XPATH, "//div[contains(text(),'Surname')]/following-sibling::div", "gvari")
    __street = Input(By.XPATH, "//div[contains(text(),'Street')]/following-sibling::div", "qucha")
    __number_button_up = \
        Button(By.XPATH, "//div[contains(text(),'Number')]/following-sibling::div//button[contains(@class,'button--up')]", "magla")
    __slider_age = Slider(By.XPATH, "//div[@class='slider__handle']", "asakis slaideri")
    __zip = Input(By.XPATH, "//div[contains(text(),'Zip')]/following-sibling::div", "zipi")
    __city = Input(By.XPATH, "//div[contains(text(),'City')]/following-sibling::div", "qalaqi")
    __country = Button(By.XPATH, "//div[contains(text(),'Country')]/following-sibling::div", "qveynebi")
    __georgia = Button(By.XPATH, "//div[@class='flag flag-ge country-dropdown__flag-item']", "saqartvelo")
    __box_button_up = Button(By.XPATH, "//div[contains(text(),'Box')]/following-sibling::div//button[contains(@class,'button--up')]", "magla box")
    __day_drop_down = Button(By.XPATH, "//div[contains(text(),'Day')]", "dge")
    __day_picker = "//div[contains(@class,'container--day')]//div[normalize-space()='{}']"
    __month_drop_down = Button(By.XPATH, "//div[contains(text(),'Month')]", "dge")
    __mount = "//div[contains(@class,'container--month')]//div[normalize-space()='{}']"
    __year_drop_down = Button(By.XPATH, "//div[contains(text(),'Year')]", "dge")
    __year = "//div[contains(@class,'container--year')]//div[normalize-space()='{}']"

    def fill_first_name(self, value):
        self.__first_name.clear_and_fill(value)

    def check_mr(self):
        self.__title.click()
        self.__mr.click()

    def fill_surname(self, value):
        self.__surname.clear_and_fill(value)

    def fill_street(self, value):
        self.__street.clear_and_fill(value)

    def press_number_up(self, count):
        self.__number_button_up.multiple_click(count)

    def move_slider(self):
        self.__slider_age.
