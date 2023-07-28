
from managers.DriverManager import DriverManager
from utils.DriverUtils import DriverUtils


class AlertUtils:
    @staticmethod
    def accept():
        DriverUtils.wait_for_alert_visible()
        alert = DriverManager.get_driver().switch_to.alert
        alert.accept()

    @staticmethod
    def get_text():
        alert = DriverManager.get_driver().switch_to.alert
        return alert.text

