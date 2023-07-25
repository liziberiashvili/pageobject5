from elements.button import Button
from elements.buttonID import ButtonId
from elements.element import Element
from elements.elementID import ElementId


class RegistrationPage:
    __create_a_new_accaunt = Button("//a[normalize-space()='Create a new account']", "registraciaze gadasasvlelad")
    __first_name = ElementId("user[first_name]", "saxelis shesavsebi")
    __last_name = ElementId("user[last_name]", "gvaris shesavsebi")
    __email1 = ElementId("user[email]", "imeilis shesavsebi")
    __password1 = ElementId("user[password]", "parolis shesavsebi")
    __check_box = ButtonId("user[terms]", "mosanishni checkboxi")
    __sign_up = Button("//button[@type='submit']", "singup gilaki")
    __product_element = Element("//h2[@class='collections__heading']", "mtavari gverdis elementi registracis mere")
    __profile_drop_down = Button("//i[@class='fa fa-caret-down']", "profilis dropdauni")
    __sing_out = Button("//a[normalize-space()='Sign Out']", "gamosvlis gilaki")
    __sing_in = Button("//a[normalize-space()='Sign In']", "loginshi shesvlis gilaki")
    __email2 = ElementId("user[email]", "imeilis shesavsebi")
    __password2 = ElementId("user[password]", "parolis shesavsebi")
    __sing_in_button = Button("//button[@type='submit']", "shesvlis gilaki")
    __product_element1 = Element("//h2[@class='collections__heading']", "mtavari gverdis elementi loginis mere")

    def create_new_accaunt_button(self):
        return self.__create_a_new_accaunt.find_element()

    def first_name_fild(self):
        return self.__first_name.find_element()

    def last_name_fild(self):
        return self.__last_name.find_element()

    def email_fild(self):
        return self.__email1.find_element()

    def password_fild(self):
        return self.__password1.find_element()

    def check_box_button(self):
        return self.__check_box.find_element()

    def sing_up_button(self):
        return self.__sign_up.find_element()

    def product_element_main_page(self):
        return self.__product_element.find_element()

    def profile_drop_down_button(self):
        return self.__profile_drop_down.find_element()

    def sing_out_button(self):
        return self.__sing_out.find_element()

    def sing_in_button(self):
        return self.__sing_in.find_element()

    def email_fild_2(self):
        return self.__email2.find_element()

    def password_fild_2(self):
        return self.__password2.find_element()

    def sing_in_button_2(self):
        return self.__sing_in_button.find_element()

    def product_element_main_page_2(self):
        return self.__product_element1.find_element()
