import pdb

class BookLibraryManagementSystem:
    def __init__(self):
        self.library = {}

    def add_book(self, book):
        self.library[book.title] = book
         
    def checkout_book(self, book):
        title = book.title
        if not book.available:
            raise Exception(f"{title} has been checked out and is not available.")
        self.library[title].available = False

    def remove_book(self, book):
        if book.title in self.library.keys():
            self.library.pop(book.title)
        else:
            raise Exception(f"{book.title} does not exist in our library and cannot be removed.")

