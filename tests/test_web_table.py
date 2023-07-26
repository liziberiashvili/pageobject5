import time

from pages.webtables_page import WebTablePage

class TestWebTable:
    def test_manipulate_on_webtable(self):
        web_tables_page = WebTablePage()
        web_tables_page.click_add_button()
        web_tables_page.modal_body_is_visible()
        web_tables_page.send_text_first_name_field()
        web_tables_page.send_text_last_name_field()
        web_tables_page.send_text_email_field()
        web_tables_page.send_text_age_field()
        web_tables_page.send_text_salary_field()
        web_tables_page.send_text_department_field()
        web_tables_page.click_submit_button()
        assert web_tables_page.edit_info_modal_body_is_visible(), "failed"
        web_tables_page.click_edit_button()
        web_tables_page.edit_info_modal_body_is_visible()
        web_tables_page.clear_first_name_data()
        web_tables_page.edit_first_name_data()
        web_tables_page.clear_last_name_data()
        web_tables_page.edit_last_name_field()
        web_tables_page.clear_salary_field()
        web_tables_page.edit_salary_field()
        web_tables_page.click_submit_button()

        web_tables_page.delete_field()






