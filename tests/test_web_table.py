import time

from data.User import User
from pages.webtables_page import WebTablePage
from teststeps.WebTablesSteps import WebTablesSteps


class TestWebTable:
    def test_manipulate_on_webtable(self):
        email = "liziberiashvili98@gmail.com"
        web_tables_page = WebTablePage()
        web_tables_page.click_add_button()
        user = User(faker.get_name(), "wdasdd@gmail.com", 21, 3333333, "dsads")
        WebTablesSteps.fill_user_fields(user)
        web_tables_page.click_submit_button()
        assert web_tables_page.is_email_visible(email)
        web_tables_page.click_edit_button()
        assert web_tables_page.edit_info_modal_body_is_visible(), "failed"
        email2 = "wsdasds@gmail.com"
        WebTablesSteps.fill_user_fields()
        assert web_tables_page.is_email_visible(email2)
        web_tables_page.delete_field()
