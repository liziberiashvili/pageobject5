from elements.Image import Image
from elements.TextField import TextField


class BooksPage:
    __book_images = Image("(//img[@alt='image'])", "Books Images")
    __book_titles = TextField("//div[@class='action-buttons']", "Book Titles")
    __book_authors = TextField("//div[@role='row' and @class='rt-tr -odd' or @class = 'rt-tr -even']/child::*[3]",
                               "Book Authors")
    __book_publishers = TextField("//div[@role='row' and @class='rt-tr -odd' or @class = 'rt-tr -even']/child::*[4]",
                                  "Book Publishers")

    def get_book_images(self):
        return self.__book_images.find_elements()

    def get_book_titles(self):
        return self.__book_titles.find_elements()

    def get_book_authors(self):
        return self.__book_authors.find_elements()

    def get_book_publishers(self):
        return self.__book_publishers.find_elements()
