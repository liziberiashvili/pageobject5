from datetime import datetime, timedelta

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element

from elements.input import Input
from elements.slider import Slider
from managers.DriverManager import DriverManager
from utils.DriverUtils import DriverUtils


class PersonalDetailsPage:
    __first_name = Input(By.XPATH, "//div[contains(text(),'First name')]/following-sibling::div//input", "first_name")
    __title = Button(By.XPATH, "//div[contains(text(),'Title')]/following-sibling::div", "title")
    __mrs = Button(By.XPATH, "//div[normalize-space()='Mrs']", "Mrs")
    __surname = Input(By.XPATH, "//div[contains(text(),'Surname')]/following-sibling::div//input", "surname")
    __street = Input(By.XPATH, "//div[contains(text(),'Street')]/following-sibling::div//input", "street")
    __number_button_up = \
        Button(By.XPATH,
               "//div[contains(text(),'Number')]/following-sibling::div//button[contains(@class,'button--up')]",
               "up_button")
    __slider_element = Slider(By.XPATH, "//div[@class='personal-details__td-cell age-property']"
                                        "//div[@class='personal-details__td-value']", "slider_element")
    __slider = Slider(By.XPATH, "//div[@class='slider__handle']", "slider")
    __slider_age = Slider(By.XPATH, "//div[@class='slider__handle' and @style='left: 50%;']", "slider_age")
    __zip = Input(By.XPATH, "//div[contains(text(),'Zip')]/following-sibling::div//input", "zip")
    __city = Input(By.XPATH, "//div[contains(text(),'City')]/following-sibling::div//input", "city")
    __country = Button(By.XPATH, "//div[contains(text(),'Country')]/following-sibling::div", "country")
    __georgia = Button(By.XPATH, "//div[@class='flag flag-ge country-dropdown__flag-item']", "georgia")
    __box_button_up = Button(By.XPATH,
                             "//div[contains(text(),'Box')]/following-sibling::div//button[contains(@class,"
                             "'button--up')]", "up_button_box")
    __day_drop_down = Button(By.XPATH, "//div[contains(text(),'Day')]", "day")
    __day_picker = "//div[contains(@class,'container--day')]//div[normalize-space()='{}']"
    __month_drop_down = Button(By.XPATH, "//div[contains(text(),'Month')]", "month")
    __month = "//div[contains(@class,'container--month')]//div[normalize-space()='{}']"
    __year_drop_down = Button(By.XPATH, "//div[contains(text(),'Year')]", "year")
    __year = "//div[contains(@class,'container--year')]//div[normalize-space()='{}']"
    __gender = Button(By.XPATH, "//div[@class='toggle-button toggle-button--right']", "gender")
    __next_button = Button(By.XPATH, "//button[normalize-space()='Next']", "next_button")
    __page_indicator = Element(By.XPATH, "//div[@class='page-indicator']", "page_indicator")

    def fill_first_name(self, value):
        DriverManager.get_driver().implicitly_wait(15)
        self.__first_name.clear_and_fill(value)

    def check_mrs(self):
        self.__title.click()
        self.__mrs.click()

    def fill_surname(self, value):
        self.__surname.clear_and_fill(value)

    def fill_street(self, value):
        self.__street.clear_and_fill(value)

    def press_number_up(self, count):
        self.__number_button_up.multiple_click(count)

    def move_slider(self):
        slider_xpath = "//div[@class='personal-details__td-cell age-property']//div[@class='personal-details__td-value']"
        slider_button_xpath = "//div[@class='slider__handle']"
        slider_element = DriverManager.get_driver().find_element(By.XPATH, slider_xpath)
        slider_button = DriverManager.get_driver().find_element(By.XPATH, slider_button_xpath)
        desired_age = 24
        max_age = 200
        slider_width = slider_element.size['width']
        position = (desired_age / max_age) * slider_width
        action = ActionChains(DriverManager.get_driver())
        action.click_and_hold(slider_button).move_by_offset(position, 0).release().perform()


    def fill_zip_code(self, value):
        self.__zip.clear_and_fill(value)

    def fill_city(self, value):
        self.__city.clear_and_fill(value)

    def check_georgia_as_a_country(self):
        self.__country.click()
        self.__georgia.click()

    def check_box_button_up(self):
        self.__box_button_up.click()


    def pick_birth_day(self):
        self.__day_drop_down.click()
        day = Button(By.XPATH, self.__day_picker.format(birth_day), "birth_day")
        day.click()

    def pick_month(self):
        self.__month_drop_down.click()
        month = Button(By.XPATH, self.__month.format(birth_month), "month")
        month.click()

    def pick_year(self):
        self.__year_drop_down.click()
        year = Button(By.XPATH, self.__year.format(birth_year), "year")
        year.click()

    def pick_gender(self):
        self.__gender.click()

    def click_next_button(self):
        self.__next_button.click()

    def page_indicator_is_opened(self):
        self.__page_indicator.is_visible()
