import random
import time

from pages.SelectablePage import SelectPage


class TestBtnSelected:
    def test_select_button(self):
        select_page = SelectPage()
        unselected_buttons = select_page.find_btns()
        random_int = random.randint(1, len(unselected_buttons))
        for i in range(random_int):
            unselected_buttons[i].click()
            time.sleep(3)
        selected_buttons = select_page.find_selected_btns()
        assert len(selected_buttons) == random_int


