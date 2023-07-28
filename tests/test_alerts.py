from pages.alerts_page import AlertPage
from utils.DriverUtils import DriverUtils
from utils.alerts_utils import AlertUtils


class TestAlerts:
    def test_alerts_visibility(self):
        alert_page = AlertPage()
        assert alert_page.is_visible()
        alert_page.click_alert_button()
        assert AlertUtils.get_text() == "You clicked a button"
        AlertUtils.accept()
        alert_page.click_timer_alert_button()
        DriverUtils.wait_for_alert_visible()
        assert AlertUtils.get_text() == "This alert appeared after 5 seconds"
        AlertUtils.accept()
        alert_page.click_confirm_button()
        alert_page.click_prompt_button()

