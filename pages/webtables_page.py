from selenium.webdriver.common.by import By

from elements.button import Button
from elements.element import Element
from elements.input import Input


class WebTablePage:
    __add_data = Button("//button[@id='addNewRecordButton']", "add_data")
    __edit_data = Button("//span[@id='edit-record-4']//*[name()='svg']", "edit_data")
    __delete_data = Button(
        "//span[@id='delete-record-4']//*[name()='svg']//*[name()='path' and contains(@d,'M864 256H7')]",
        "delete_data_")
    __add_info_modal_body = Element("//div[@class='modal-body']", "modal_body")
    __first_name_field = Input("//input[@id='firstName']", "firstname")
    __last_name_field = Input("//input[@id='lastName']", "lastname")
    __email_field = Input(By.XPATH, "//input[@id='userEmail']", "email")
    __age_field = Input(By.XPATH, "//input[@id='age']", "age")
    __salary_field = Input(By.XPATH, "//input[@id='salary']", "salary")
    __department_field = Input(By.XPATH, "//input[@id='department']", "department")
    __submit_button = Button("//button[@id='submit']", "submit-button")
    __edit_info_modal_body = Element("//div[@class='modal-body']", "edit_info_modal_body")
    __email_xpath = "//div[normalize-space()='{}']"

    def click_add_button(self):
        return self.__add_data.click()

    def modal_body_is_visible(self):
        return self.__add_info_modal_body.is_visible()

    def fill_first_name(self, value):
        return self.__first_name_field.clear_and_fill(value)

    def fill_last_name(self, value):
        return self.__last_name_field.clear_and_fill(value)

    def fill_email(self, email):
        return self.__email_field.clear_and_fill(email)

    def fill_age(self, value):
        return self.__age_field.send_text(value)

    def fill_salary(self, value):
        return self.__salary_field.clear_and_fill(value)

    def fill_department(self, value):
        return self.__department_field.send_text(value)

    def click_submit_button(self):
        return self.__submit_button.click()

    def click_edit_button(self):
        return self.__edit_data.click()

    def edit_info_modal_body_is_visible(self):
        return self.__edit_info_modal_body.is_visible()

    def delete_field(self):
        return self.__delete_data.click()

    def is_email_visible(self, value):
        email_element = Element(self.__email_xpath.format(value), "Email")
        return email_element.is_visible()
