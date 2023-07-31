import time

from data.user_model import Registration
from pages.timer_page import TimerPage
from teststeps.TimerPageSteps import TimerPageSteps


class TestTimer:
    def test_timer(self):
        timer_page = TimerPage()
        user = Registration("ЛЛЛЛЛЛЛЛlizi@LIZI@lizi@1234ЛЛЛЛЛЛЛ", "liziberiashvili98", "gmail")
        timer_page_steps = TimerPageSteps()
        time.sleep(5)
        timer_page_steps.fill_registration(user)
        assert timer_page.avatar_box_is_displayed()
        time.sleep(4)
        timer_page_steps.fill_registration2()
        time.sleep(4)
        timer_page_steps.upload_file()

