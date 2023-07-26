from pages.radio_button_page import RadioButtonPage


class TestRadioButton:
    def test_radio_button(self):
        value = "Impressive"
        radio_button_page = RadioButtonPage()
        radio_button_page.click_radio_button(value)
        assert radio_button_page.get_text() == value
