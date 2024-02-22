from Book import Books  # Importing the Books class from the Book module
import random
import re

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
                file.write(f"{book.id},{book.title},{book.author},{book.isbn},{book.price},{book.copyright_date}\n")

    def getAllBooks(self): # Return all books in the library
        self.loadBooks()
        return self.Books_in_my_library
    
    def removeBook(self): # Remove a book by its ID
        id_to_remove = int(input("What book would you like to remove (Enter ID): "))
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
    
    def updateBookById(self): # Update book information by its ID
        id = int(input("What book would you like to update (Enter ID): "))
        for book in self.Books_in_my_library:
            if book.id == id:
                while True:
                    updated_book_info = self.promptBookInfo(book)
                    book.title, book.author, book.price, book.copyright_date = updated_book_info
                    self.saveBooks()
                    return "Book updated successfully."
        return (f"Book ID: {id} was not found.\n")

    def createBook(self): # Create a new book
        while True:
            book_info = self.promptBookInfo()
            if book_info:
                id = len(self.Books_in_my_library) + 1
                title, author, price, copyright_date = book_info
                # Generate a unique ISBN and create a new book object
                new_book = Books(id, title, author, self.generateUniqueIsbn(), price, copyright_date)
                self.Books_in_my_library.append(new_book)
                self.saveBooks()
                return "Book created successfully."

    def promptBookInfo(self, book=None): # Prompt for book information
        while True:
            prompt = "Enter the new information for a new Book:" if book is None else f"Enter the new information for the Book: {book.title}"
            print(prompt)
            title = self.validateInput("Enter new title: ", "Title", lambda s: all(c.isalnum() or c in (" ", "'") for c in s))
            author = self.validateInput("Enter new author: ", "Author", lambda s: all(c.isalpha() or c in (" ", "'") for c in s))
            price = self.validateFloatInput("Enter new price: ", "Price", lambda s: float(s) > 0)
            copyright_date = self.validateDateInput("Enter new published date (MM-DD-YYYY): ", lambda s: re.match(r'\d{2}-\d{2}-\d{4}', s))
            
            if title and author and price and copyright_date:
                return (title, author, price, copyright_date)

    def validateInput(self, prompt, field_name, validation_func): # Validate user input
        while True:
            user_input = input(prompt)
            if user_input and validation_func(user_input):
                return user_input
            print(f"{field_name} cannot be empty and must contain only valid characters.")

    def validateFloatInput(self, prompt, field_name, validation_func): # Validate float input
        while True:
            user_input = input(prompt)
            try:
                if validation_func(user_input):
                    return float(user_input)
                else:
                    print("Price must be positive.")
            except ValueError:
                print(f"Invalid {field_name} format. Please enter a valid {field_name.lower()}.")

    def validateDateInput(self, prompt, validation_func): # Validate date input
        while True:
            user_input = input(prompt)
            if validation_func(user_input):
                month, day, year = map(int, user_input.split('-'))
                if 1 <= month <= 12 and 1 <= day <= 31 and 1800 <= year <= 2025:
                    if month in [4, 6, 9, 11] and day > 30:
                        print("Invalid day for the given month.")
                    elif month == 2:
                        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                            if day > 29:
                                print("Invalid day for the given month.")
                        elif day > 28:
                            print("Invalid day for the given month.")
                    else:
                        return user_input
                else:
                    print("Invalid date range.")
            else:
                print("Invalid date format. Use MM-DD-YYYY format.")

    def generateUniqueIsbn(self): # Generate a unique ISBN
        while True:
            isbn = str(978) + str(random.randint(1000000000, 9999999999))
            if isbn not in self.existing_isbns:
                return isbn

    def menu(self): # Print menu options
        print("1 Show all the books")
        print("2 Create a book")
        print("3 Remove a book")
        print("4 Find book(s) by string")
        print("5 Update a book")
        print("6 to quit")
