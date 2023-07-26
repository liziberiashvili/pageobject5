import time

from data.User import User
from pages.webtables_page import WebTablePage
from teststeps.WebTablesSteps import WebTablesSteps


class TestWebTable:
    def test_manipulate_on_webtable(self):
        email = "liziberiashvili98@gmail.com"
        email2 = "xvtisochxeidze@gmail.com"
        web_tables_page = WebTablePage()
        web_tables_page.click_add_button()
        user1 = User("lizi", "beriashvili", email, 21, 3333333, "software testing")
        WebTablesSteps.fill_user_fields(user1)
        assert web_tables_page.is_email_visible(email)
        web_tables_page.click_edit_button()
        user2 = User("gtrght", "hgrkgnr", email2, 23, 48435, "sgjhgt")
        WebTablesSteps.fill_user_fields(user2)
        assert web_tables_page.is_email_visible(email2)
        web_tables_page.delete_field()
