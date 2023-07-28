from selenium.webdriver.common.by import By

from elements.button import Button
from pages.base_form import BaseForm


class AlertPage(BaseForm):
    __alert_button = Button(By.XPATH, "//button[@id='alertButton']", "alert_button")
    __timer_alert_button = Button(By.XPATH, "//button[@id='timerAlertButton']", "timer_alert_button")
    __confirm_button = Button(By.XPATH, "//button[@id='confirmButton']", "confirm_button")
    __prompt_button = Button(By.XPATH, "//button[@id='promtButton']", "prompt_button")

    def __init__(self):
        super().__init__(By.XPATH, "//button[@id='alertButton']", "unique_element")

    def click_alert_button(self):
        self.__alert_button.click()

    def click_timer_alert_button(self):
        self.__timer_alert_button.click()

    def click_confirm_button(self):
        self.__confirm_button.click()

    def click_prompt_button(self):
        self.__prompt_button.click()
