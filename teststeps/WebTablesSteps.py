from pages.webtables_page import WebTablePage


class WebTablesSteps:

    @staticmethod
    def fill_user_fields(user):
        web_tables_page = WebTablePage()
        web_tables_page.fill_first_name(user.first_name)
        web_tables_page.fill_last_name(user.last_name)
        web_tables_page.fill_email(user.email)
        web_tables_page.fill_age(user.age)
        web_tables_page.fill_salary(user.salary)
        web_tables_page.fill_department(user.department)
        web_tables_page.click_submit_button()
