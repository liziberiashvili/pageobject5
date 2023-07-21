from elements.button import Button


class SelectPage:

    __slectbtn = Button("//li[@class='mt-2 list-group-item list-group-item-action']", "gilakebi")
    __selectedbtn = Button("//li[@class='mt-2 list-group-item active list-group-item-action']", "monishnuli gilakebi")

    def find_btns(self):
        return self.__slectbtn.find_elements()

    def find_selected_btns(self):
        return self.__selectedbtn.find_elements()