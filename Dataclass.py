import random
import re
from Book import Books  # Importing the Books class from the Book module

class BookShelf:
    def __init__(self):
        # Initialize file name, list of books, and load existing books
        self.filename = "books.txt"
        self.Books_in_my_library = []
        self.loadBooks()
        # Create a set of existing ISBNs for validation
        self.existing_isbns = {book.isbn for book in self.Books_in_my_library}

    def loadBooks(self): # Load books from the text file
        self.Books_in_my_library = []
        with open(self.filename, "r") as file:
            for line in file:
                # Split the line and create Book objects
                id, title, author, isbn, price, copyright_date = map(str.strip, line.strip().split(","))
                book = Books(int(id), title, author, isbn, float(price), copyright_date)
                self.Books_in_my_library.append(book)

    def saveBooks(self): # Save books to the text file
        with open(self.filename, "w") as file:
            for book in self.Books_in_my_library:
                file.write(f"{book.id},{book.title},{book.author},{book.isbn},{float(book.price):.2f},{book.copyright_date}\n")

    def getAllBooks(self): # Return all books in the library
        self.loadBooks()
        return self.Books_in_my_library
    
    def removeBook(self, id_to_remove): # Remove a book by its ID
        for book in self.Books_in_my_library[:]:
            if book.id == id_to_remove:
                self.Books_in_my_library.remove(book)
                self.saveBooks()
                return f"You deleted {book}"
        return None

    def searchBooks(self, string): # Search books by title, author, or copyright date
        found_books = []
        for book in self.Books_in_my_library:
            if (string.lower() in book.title.lower()) or (string.lower() in book.author.lower()) or (string in book.copyright_date):
                found_books.append(book)
        return found_books
    
    def findBook(self, id):
        # load all things first
        self.loadBooks()

        # find the matching thing using the id number by iterating through the list. when found, return it
        for book in self.Books_in_my_library:
            if book.id == id:
                return book
        return None
    
    def updateBookById(self, id, book_info): # Update book information by its ID
        errors = self.validateBookInfo(*book_info)
        if errors:
            return errors

        for book in self.Books_in_my_library:
            if book.id == id:
                book.title, book.author, book.price, book.copyright_date = book_info
                self.saveBooks()
                return "Book updated successfully."
        return (f"Book ID: {id} was not found.")

    def createBook(self, book_info): # Create a new book
        id = len(self.Books_in_my_library) + 1
        title, author, price, copyright_date = book_info
        
        # Validate book information
        validation_result = self.validateBookInfo(title, author, price, copyright_date)
        if isinstance(validation_result, list):
            # If validation errors exist, return the list of errors
            return validation_result
        
        # If validation successful, create a new book
        new_book = Books(id, title, author, self.generateUniqueIsbn(), price, copyright_date)
        self.Books_in_my_library.append(new_book)
        self.saveBooks()
        return "Book created successfully."

    def validateBookInfo(self, title, author, price, copyright_date):
        errors = []

        if not isinstance(title, str) or not title.strip():
            errors.append("Invalid title. Please enter a valid title.")
        if not isinstance(author, str) or not author.strip():
            errors.append("Invalid author. Please enter a valid author.")
        try:
            price = float(price)
            if price <= 0:
                errors.append("Price must be a positive number. Please enter a valid price.")
        except ValueError:
            errors.append("Invalid price format. Price must be a number.")

        if not re.match(r'\d{2}-\d{2}-\d{4}', copyright_date):
            errors.append("Invalid date format. Use MM-DD-YYYY format.")
        else:
            month, day, year = map(int, copyright_date.split('-'))
            if not (1 <= month <= 12 and 1 <= day <= 31 and 1800 <= year <= 2025):
                errors.append("Invalid date range.")

            if month in [4, 6, 9, 11] and day > 30:
                errors.append("Invalid day for the given month.")
            elif month == 2:
                if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                    if day > 29:
                        errors.append("Invalid day for the given month.")
                elif day > 28:
                    errors.append("Invalid day for the given month.")

        return errors if errors else "Validation successful."

    def generateUniqueIsbn(self): # Generate a unique ISBN
        while True:
            isbn = str(978) + str(random.randint(1000000000, 9999999999))
            if isbn not in self.existing_isbns:
                return isbn
