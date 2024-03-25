import re
from Book import Book  # Assuming Book class is defined in Book.py

class BookShelf:
    def __init__(self):
        # Initialize file name, list of books, and load existing books
        self.filename = "books.txt"
        self.Books_in_my_library = []
        self.loadBooks()
        # Create a set of existing ISBNs for validation
        self.existing_isbns = {book.isbn for book in self.Books_in_my_library}

    def loadBooks(self):
        # Load books from the text file
        self.Books_in_my_library = []
        with open(self.filename, "r") as file:
            for line in file:
                # Split the line and create Book objects
                id, title, author, isbn, price, copyright_date = map(str.strip, line.strip().split(","))
                book = Book(int(id), title, author, isbn, float(price), copyright_date)
                self.Books_in_my_library.append(book)

    def saveBooks(self):
        # Save books to the text file
        with open(self.filename, "w") as file:
            for book in self.Books_in_my_library:
                file.write(f"{book.id},{book.title},{book.author},{book.isbn},{book.price},{book.copyright_date}\n")

    def getAllBooks(self):
        # Return all books in the library
        self.loadBooks()
        return self.Books_in_my_library
    
    def removeBook(self, id_to_remove):
        # Remove a book by its ID
        for book in self.Books_in_my_library[:]:
            if book.id == id_to_remove:
                self.Books_in_my_library.remove(book)
                self.saveBooks()
                return f"You deleted {book}"
        return None

    def searchBooks(self, string):
        # Search books by title, author, isbn, price, or copyright date
        found_books = []
        for book in self.Books_in_my_library:
            if (string.lower() in book.title.lower()) \
                or (string.lower() in book.author.lower()) \
                or (isinstance(book.copyright_date, str) and string in book.copyright_date) \
                or (isinstance(book.isbn, str) and string in book.isbn):
                found_books.append(book)
        return found_books

    
    def findBook(self, id):
        # Find a book by its ID
        self.loadBooks() # Ensure books are loaded
        for book in self.Books_in_my_library:
            if book.id == id:
                return book
        return None
    
    def updateBook(self, id, title, author, isbn, price, copyright_date):
        # Update book information by its ID
        errors = self.validateBookInfo(title, author, isbn, price, copyright_date)
        if errors:
            return errors

        for stored_book in self.Books_in_my_library:
            if stored_book.id == id:
                # Adjusting the order of parameters
                stored_book.title = title
                stored_book.author = author
                stored_book.isbn = isbn
                stored_book.price = price
                stored_book.copyright_date = copyright_date
                self.saveBooks()
                return "Book updated successfully."
        return f"Book ID: {id} was not found."

    def createBook(self, title, author, isbn, price, copyright_date):
        # Create a new book
        errors = self.validateBookInfo(title, author, isbn, price, copyright_date)
        if errors:
            return errors

        # Check if ISBN already exists
        if isbn in self.existing_isbns:
            return "A book with the same ISBN already exists in the library."

        id = len(self.Books_in_my_library) + 1
        
        # If validation successful, create a new book
        new_book = Book(id, title, author, isbn, price, copyright_date)
        self.Books_in_my_library.append(new_book)
        self.existing_isbns.add(isbn) 
        self.saveBooks()
        return "Book created successfully."


    def validateBookInfo(self, title, author, isbn, price, copyright_date):
        # Validate book information
        errors = []

        if not isinstance(title, str) or not title.strip():
            errors.append("Invalid title. Please enter a valid title.")
        if not isinstance(author, str) or not author.strip():
            errors.append("Invalid author. Please enter a valid author.")
        if not isbn or not re.match(r'^\d{13}$', isbn):
            errors.append("Invalid ISBN. Please enter a valid 13-digit ISBN.")
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

        return errors if errors else None
