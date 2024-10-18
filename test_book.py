import unittest
import pdb
from book import Book
from book_library_management_system import BookLibraryManagementSystem

class TestBook(unittest.TestCase):

    def test_book_is_created_with_title_author_isbn_and_available(self):
        kvg = Book("Galapagos", "Kurt Vonnegut", 12345, True)
        self.assertEqual(kvg.title, "Galapagos")
        self.assertEqual(kvg.author, "Kurt Vonnegut")
        self.assertEqual(kvg.isbn, 12345)
        self.assertEqual(kvg.available, True)

    def test_book_must_have_string_as_title(self):
        with self.assertRaises(TypeError) as context:
            Book({}, "Kurt Vonnegut", "123456", True)
        self.assertEqual(str(context.exception), "Expected title to be of type str.")

    def test_book_must_have_string_as_author(self):
        with self.assertRaises(TypeError) as context:
            Book("Galapagos", [], "123456", True)
        self.assertEqual(str(context.exception), "Expected author to be of type str.")

    def test_book_must_have_int_as_isbn(self):
        with self.assertRaises(TypeError) as context:
            Book("Galapagos", "Kurt Vonnegut", "cheese", True)
        self.assertEqual(str(context.exception), "Expected isbn to be of type int.")

    def test_book_must_have_bool_as_available(self):
        with self.assertRaises(TypeError) as context:
            Book("Galapagos", "Kurt Vonnegut", 12345, "Cheese")
        self.assertEqual(str(context.exception), "Expected available to be of type bool.")                

if __name__ == '__main__':
    unittest.main()