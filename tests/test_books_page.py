from pages.BooksPage import BooksPage
from teststeps.BooksPageSteps import BooksPageSteps


class TestBooksPage:

    def test_content_is_visible(self):
        books_page = BooksPage()
        books_titles = books_page.get_book_titles()
        books_images = books_page.get_book_images()
        books_authors = books_page.get_book_authors()
        books_publishers = books_page.get_book_publishers()
        assert BooksPageSteps.is_elements_empty(books_publishers)
        assert BooksPageSteps.is_elements_empty(books_authors)
        assert BooksPageSteps.is_elements_empty(books_titles)
        assert BooksPageSteps.is_elements_empty(books_images)
