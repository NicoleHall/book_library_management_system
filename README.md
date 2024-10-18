### **CHAT GPT PROMPT**  
Can you give me a small project to complete in Python? It should include tests. Do not provide code or solutions. 

---
### **CHAT GPT RESPONSE**  
Create a **"Book Library Management System"** project in Python. Here are the main features to include:

1. **Classes and Methods**:
   - Create a `Book` class with attributes like `title`, `author`, `isbn`, and `available` (boolean indicating if the book is available).
   - Create a `Book Library Management System` class with methods to add books, remove books, and check out books to users. When a book is lent, mark it as unavailable.

2. **Tests**:
   - Write unit tests to verify the functionality of each method:
     - Test adding a book.
     - Test removing a book.
     - Test lending a book and updating its availability status.

###### This will give you practice with classes, basic CRUD operations, and using Python's `unittest` module to validate each feature.
---
### **THE BOOK LIBRARY MANAGEMENT SYSTEM APP**  
To run the tests:
navigate to project directory in the terminal, run `python -m unittest discover` to run tests