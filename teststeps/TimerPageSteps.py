import time

from pages.timer_page_1 import TimerPage1
from pages.timer_page_2 import TimerPage2


class TimerPageSteps:
    @staticmethod
    def fill_registration1(user):
        timer_page1 = TimerPage1()
        timer_page1.remove_red_header()
        timer_page1.fill_password(user.password)
        timer_page1.fill_email(user.email)
        timer_page1.fill_domain(user.domain)
        time.sleep(5)
        timer_page1.click_dropdown()
        timer_page1.click_email_finish()
        timer_page1.click_checkbox()
        timer_page1.click_next_button()

    @staticmethod
    def fill_registration2():
        timer_page2 = TimerPage2()
        path = "/Users/lizi/avatar.png"
        timer_page2.unselect_all_interest()
        timer_page2.check_purple_interest()
        timer_page2.check_cotton_interest()
        timer_page2.check_drywall_interest()
        time.sleep(5)
        timer_page2.find_upload_image_button()
        timer_page2.upload_profile_image(path)
        timer_page2.press_enter()
        time.sleep(10)
        timer_page2.click_next_button()
