class BooksPageSteps:
    @staticmethod
    def is_elements_empty(elements):
        is_displayed = 0
        for i in elements:
            if not i.is_displayed():
                is_displayed += 1
        if is_displayed == 0 and len(elements) != 0:
            return True


