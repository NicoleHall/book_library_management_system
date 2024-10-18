import unittest
import pdb
from book import Book
from book_library_management_system import BookLibraryManagementSystem

class TestBookLibraryManagementSystem(unittest.TestCase):

    def test_library_is_an_empty_dict_when_BookLibraryManagementSystem_is_instantiated(self):
        new_lib = BookLibraryManagementSystem()
        self.assertEqual(new_lib.library, {})

    def test_a_book_is_added_to_library(self):
        new_lib = BookLibraryManagementSystem()
        kvg = Book("Galapagos", "Kurt Vonnegut", 12345, True)
        new_lib.add_book(kvg)
        self.assertEqual(new_lib.library["Galapagos"].title, "Galapagos")

    def test_a_book_can_be_checked_out(self):
        new_lib = BookLibraryManagementSystem()
        kvg = Book("Galapagos", "Kurt Vonnegut", 12345, True)
        kvpp = Book("Player Piano", "Kurt Vonnegut", 12347, True)
        new_lib.add_book(kvg)
        new_lib.add_book(kvpp)
        new_lib.checkout_book(kvg)
        self.assertEqual(new_lib.library[kvg.title].available, False)
        self.assertEqual(new_lib.library[kvpp.title].available, True)

    def test_a_book_cannot_be_checked_out_if_available_is_false(self):
        new_lib = BookLibraryManagementSystem()
        kvg = Book("Galapagos", "Kurt Vonnegut", 12345, True)
        new_lib.add_book(kvg)
        new_lib.checkout_book(kvg)
        self.assertEqual(new_lib.library[kvg.title].available, False)
        with self.assertRaises(Exception) as context:
            new_lib.checkout_book(kvg)
        self.assertEqual(str(context.exception), "Galapagos has been checked out and is not available.")

    def test_a_book_can_be_removed(self):
        new_lib = BookLibraryManagementSystem()
        kvg = Book("Galapagos", "Kurt Vonnegut", 12345, True)
        new_lib.add_book(kvg)
        new_lib.remove_book(kvg)
        self.assertNotIn(kvg.title, new_lib.library.keys())

    def test_a_book_cannot_be_removed_if_it_does_not_exist(self):
        new_lib = BookLibraryManagementSystem()
        kvg = Book("Galapagos", "Kurt Vonnegut", 12345, True)
        #add_book method intentionally not called
        with self.assertRaises(Exception) as context:
            new_lib.remove_book(kvg)
        self.assertEqual(str(context.exception), "Galapagos does not exist in our library and cannot be removed.")      

    

        