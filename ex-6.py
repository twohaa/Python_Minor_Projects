# Library Management System


# Write a Library class with no_of_books and books as two instance variables.
# Write a program to create a library from this Library class and show how you can print all books,
# add a book and get the number of books using different methods.
# Show that your program doesnt persist the books after the program is stopped!


class Library:
    def __init__(self):
        self.noOfBooks = 0
        self.books = []

    def addBooks(self, book):
        self.books.append(book)
        self.noOfBooks = len(self.books)

    def showinfo(self):
        print(f"The library has {self.noOfBooks} books.The books are: ")
        for book in self.books:
            print(book)


l1 = Library()
l1.addBooks("HYE HYE")
l1.addBooks("HYE HYE HYE")
l1.addBooks("HYE")
l1.showinfo()
