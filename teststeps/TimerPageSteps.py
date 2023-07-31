import time

from elements import element
from elements.input import Input
from pages.personal_details_page import PersonalDetailsPage
from pages.timer_page import TimerPage
from pages.interest_page import InterestPage
from utils.DriverUtils import DriverUtils


class TimerPageSteps:
    @staticmethod
    def fill_registration(user):
        timer_page1 = TimerPage()
        timer_page1.remove_red_header()
        timer_page1.fill_password(user.password)
        timer_page1.fill_email(user.email)
        timer_page1.fill_domain(user.domain)
        timer_page1.click_dropdown()
        timer_page1.click_email_finish()
        timer_page1.click_checkbox()
        timer_page1.click_next_button()

    @staticmethod
    def fill_registration2():
        timer_page2 = InterestPage()
        timer_page2.unselect_all_interest()
        timer_page2.check_purple_interest()
        timer_page2.check_cotton_interest()
        timer_page2.check_drywall_interest()
        timer_page2.find_upload_image_button()
        TimerPageSteps.upload_file()
        timer_page2.click_next_button()

    @staticmethod
    def upload_file():
        time.sleep(5)

    @staticmethod
    def fill_personal_details(user2):
        personal_details_page = PersonalDetailsPage()
        personal_details_page.fill_first_name(user2.firstname)
        personal_details_page.check_mrs()
        personal_details_page.fill_surname(user2.surname)
        personal_details_page.fill_street(user2.street)
        personal_details_page.press_number_up(count=2)
        personal_details_page.move_slider()
        personal_details_page.fill_zip_code(user2.zipcode)
        personal_details_page.fill_city(user2.city)
        personal_details_page.check_georgia_as_a_country()
        personal_details_page.check_box_button_up()
        personal_details_page.pick_birth_day(day=11)
        personal_details_page.pick_month(month="October")
        personal_details_page.pick_year(year=1998)
        personal_details_page.pick_gender()
        personal_details_page.click_next_button()
