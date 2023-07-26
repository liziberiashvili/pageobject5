from elements.button import Button
from elements.element import Element
from elements.input import Input


class WebTablePage:
    __add_data = Button("//button[@id='addNewRecordButton']", "add_data")
    __edit_data = Button("//span[@id='edit-record-4']//*[name()='svg']","edit_data")
    __delete_data = Button(
        "//span[@id='delete-record-4']//*[name()='svg']//*[name()='path' and contains(@d,'M864 256H7')]",
        "delete_data_")
    __add_info_modal_body = Element("//div[@class='modal-body']", "modal_body")
    __first_name_field = Input("//input[@id='firstName']", "firstname")
    __last_name_field = Input("//input[@id='lastName']", "lastname")
    __email_field = Input("//input[@id='userEmail']", "email")
    __age_field = Input("//input[@id='age']", "age")
    __salary_field = Input("//input[@id='salary']", "salary")
    __department_field = Input("//input[@id='department']", "department")
    __submit_button = Button("//button[@id='submit']", "submit-button")
    __edit_info_modal_body = Element("//div[@class='modal-body']", "edit_info_modal_body")

    def click_add_button(self):
        return self.__add_data.click()

    def modal_body_is_visible(self):
        return self.__add_info_modal_body.is_visible()

    def send_text_first_name_field(self):
        return self.__first_name_field.send_text(value="lizi")

    def send_text_last_name_field(self):
        return self.__last_name_field.send_text(value="Beriashvili")

    def send_text_email_field(self):
        return self.__email_field.send_text(value="liziberiashvili98@gmail.com")

    def send_text_age_field(self):
        return self.__age_field.send_text(value="24")

    def send_text_salary_field(self):
        return self.__salary_field.send_text(value="3000")

    def send_text_department_field(self):
        return self.__department_field.send_text(value="Software Testing")

    def click_submit_button(self):
        return self.__submit_button.click()

    def click_edit_button(self):
        return self.__edit_data.click()

    def edit_info_modal_body_is_visible(self):
        return self.__edit_info_modal_body.is_visible()

    def clear_first_name_data(self):
        return self.__first_name_field.clear()

    def edit_first_name_data(self):
        return self.__first_name_field.send_text(value="Xvtiso")

    def clear_last_name_data(self):
        return self.__last_name_field.clear()

    def edit_last_name_field(self):
        return self.__last_name_field.send_text(value="Chxeidze")

    def clear_salary_field(self):
        return self.__salary_field.clear()

    def edit_salary_field(self):
        return self.__salary_field.send_text(value="30000")

    def delete_field(self):
        return self.__delete_data.click()



