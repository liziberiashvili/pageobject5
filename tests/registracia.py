from faker import Faker

from pages.RegistrationPage import RegistrationPage

fake = Faker()
email = fake.email()
password = fake.password()

class TestRegistration:
    def test_registration_and_login_form(self):
        registration = RegistrationPage()
        registration.create_new_accaunt_button().click()
        registration.first_name_fild().send_keys(fake.user_name())
        registration.last_name_fild().send_keys(fake.last_name())
        registration.email_fild().send_keys(email)
        registration.password_fild().send_keys(password)
        registration.check_box_button().click()
        registration.sing_up_button().click()

        registration.profile_drop_down_button().click()
        registration.sing_out_button().click()
        registration.sing_in_button().click()
        registration.email_fild_2().send_keys(email)
        registration.password_fild_2().send_keys(password)
        registration.sing_in_button_2().click()
        assert registration.product_element_main_page().is_displayed()
        assert registration.product_element_main_page_2().is_displayed()
