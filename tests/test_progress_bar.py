import time

from pages.progress_bar_page import ProgressBarPage


class TestProgressBarFlexible:
    def test_progress_bar_start_stop(self):
        progress_bar_page = ProgressBarPage()
        progress_bar_page.click_start_button().click()
        progress_bar_page.wait_for_progress_bar_value()
        progress_bar_page.click_stop_button().click()

        assert progress_bar_page.wait_for_progress_bar_value(), "shecdoma"

        # assert TestProgressBarFlexible
        # if not TestProgressBarFlexible:
        #     raise "armushaobs"
