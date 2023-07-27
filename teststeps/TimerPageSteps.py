import time

from pages.timer_page import TimerPage


class TimerPageSteps:
    @staticmethod
    def fill_registration(user):
        timer_page = TimerPage()
        timer_page.fill_password(user.password)
        timer_page.fill_email(user.email)
        timer_page.fill_domain(user.domain)
        time.sleep(5)
        timer_page.click_dropdown()
        timer_page.click_email_finish()
        timer_page.click_checkbox()
        timer_page.click_next_button()
