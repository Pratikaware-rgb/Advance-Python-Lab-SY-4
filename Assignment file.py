class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron ID: {self.patron_id}, Name: {self.name}")
        print("Borrowed Books:", self.borrowed_books)


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print(f"Book '{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book.title)
            print(f"{patron.name} borrowed '{book.title}'.")

    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.title in patron.borrowed_books:
            book.is_borrowed = False
            patron.borrowed_books.remove(book.title)
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print(f"{patron.name} did not borrow '{book.title}'.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            book.display()

    def display_patrons(self):
        print("\nRegistered Patrons:")
        for patron in self.patrons.values():
            patron.display()



library = Library()

library.add_book(Book(101, "Python Programming", "John Smith"))
library.add_book(Book(102, "Data Structures", "Alice Brown"))
library.add_book(Book(103, "Machine Learning", "Andrew Ng"))

library.register_patron(Patron(1, "Rahul"))
library.register_patron(Patron(2, "Anita"))

library.display_books()

library.borrow_book(1, 101)
library.borrow_book(2, 102)

library.display_books()

library.return_book(1, 101)

library.display_books()
library.display_patrons()
