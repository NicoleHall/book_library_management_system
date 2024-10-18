import pdb

class Book:
    def __init__(self, title: str, author: str, isbn: int, available: bool):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available
        if not isinstance(title, str):
            raise TypeError("Expected title to be of type str.")
        if not isinstance(author, str):
            raise TypeError("Expected author to be of type str.")
        if not isinstance(isbn, int):
            raise TypeError("Expected isbn to be of type int.")
        if not isinstance(available, bool):
            raise TypeError("Expected available to be of type bool.")