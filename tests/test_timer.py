import time

from data.registration_timerPage import Registration
from pages.timer_page_1 import TimerPage1
from teststeps.TimerPageSteps import TimerPageSteps


class TestTimer:
    def test_timer(self):
        value = "00:00:00"
        timer_page = TimerPage1()
        assert timer_page.get_text_from_timer() == value
        user = Registration("ЛЛЛЛЛЛЛЛlizi@LIZI@lizi@1234ЛЛЛЛЛЛЛ", "liziberiashvili98", "gmail")
        timer_page_steps = TimerPageSteps()
        time.sleep(5)
        timer_page_steps.fill_registration1(user)
        assert timer_page.avatar_box_is_displayed()
        time.sleep(4)
        timer_page_steps.fill_registration2()
        time.sleep(4)

