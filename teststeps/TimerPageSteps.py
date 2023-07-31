import time

import pyautogui

from managers.DriverManager import DriverManager
from pages.timer_page import TimerPage
from pages.interest_page import InterestPage


class TimerPageSteps:
    @staticmethod
    def fill_registration(user):
        timer_page1 = TimerPage()
        timer_page1.remove_red_header()
        timer_page1.fill_password(user.password)
        timer_page1.fill_email(user.email)
        timer_page1.fill_domain(user.domain)
        timer_page1.click_dropdown()
        timer_page1.click_email_finish()
        timer_page1.click_checkbox()
        timer_page1.click_next_button()

    @staticmethod
    def fill_registration2():
        timer_page2 = InterestPage()
        timer_page2.unselect_all_interest()
        timer_page2.check_purple_interest()
        timer_page2.check_cotton_interest()
        timer_page2.check_drywall_interest()
        timer_page2.find_upload_image_button()
        TimerPageSteps.upload_file()

    @staticmethod
    def upload_file():
        image_file_path = r"\C:\Users\ghvti\Downloads\gasashvebi.png"
        pyautogui.write(image_file_path)
        pyautogui.press("enter")
        DriverManager.get_driver().execute_script("window.scrollTo(0,document.body.scrollHeight)")
        timer_page3 = InterestPage()
        timer_page3.click_next_button()
