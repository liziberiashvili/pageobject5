from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
from utils.DriverUtils import DriverUtils


class ProgressBarPage:
    __start_button = Button("//button[@id='startStopButton']", "start_button")
    __stop_button = Button("//button[@id='startStopButton']", "stop_button")
    __progress_bar_value = Element("//div[@role='progressbar']", 'progress_bar_value')

    def click_start_button(self):
        return self.__start_button.find_element()

    def wait_for_progress_bar_value(self):

        locator = By.XPATH, self.__progress_bar_value.locator
        attribute = "aria-valuenow"
        text = '30'
        DriverUtils.wait_for_changes(locator, attribute, text)

    def click_stop_button(self):
        return self.__stop_button.find_element()
