# Importing the necessary module and classes
from Book import Books
import random
import re

# Define a class representing a bookshelf
class BookShelf:
    # Initialize the bookshelf with predefined books
    def __init__(self):
        # Define some initial books for the bookshelf
        book1 = Books(1, "Where's Molly", "H D Carlton", 9780316069359, 16.99, "02-16-2024")
        book2 = Books(2, "Powerless", "Lauren Roberts", 9780061122415, 17.99, "11-07-2023")
        book3 = Books(3, "The Great Gatsby", "F. Scott Fitzgerald", 9780140444254, 11.47, "04-10-1925")
        book4 = Books(4, "The Hobbit", "J.R.R. Tolkien", 9780765432105, 10.99, "09-21-1937")
        book5 = Books(5, "The Hunger Games", "Suzanne Collins", 9781234567890, 11.47, "12-24-2013")

        # Store the initial books in a list
        self.Books_in_my_library = [book1, book2, book3, book4, book5]

        # Store existing ISBNs in a set for quick lookup
        self.existing_isbns = {book.isbn for book in self.Books_in_my_library}

    # Function to get all books from the bookshelf
        # Option 1
    def getAllBooks(self):
        return self.Books_in_my_library
    
    # Function to create a new book and add it to the bookshelf
        # Option 2
    def createBook(self):
        while True:
            try:
                # Call the function to prompt the user for new book information
                message = self.promptBookInfo()
                # Return the message indicating the result of the creation
                return message
            except ValueError as error:
                # If any validation fails, print the error message and continue the loop
                print(f"Error creating book: {error}\n")

    # Function to remove a book from the bookshelf based on its ID
        # Option 3
    def removeBook(self, id):
        for book in self.Books_in_my_library:
            if book.id == id:
                # If the book with the given ID is found, remove it from the bookshelf
                self.Books_in_my_library.remove(book)
                # Return a message indicating the deletion of the book
                return (f"You deleted {book}")
        # If no book with the given ID is found, return None
        return None
            
    # Function to search for books based on a string
        # Option 4
    def searchBooks(self, string):
        found_books = []
        for book in self.Books_in_my_library:
            if (string.lower() in book.title.lower()) or (string.lower() in book.author.lower()) or (string in book.copyright_date):
                found_books.append(book)
        return found_books
    
    # Function to update a book by its ID
        # Option 5
    def updateBookById(self, id):
        # Find the book with the given ID
        for book in self.Books_in_my_library:
            if book.id == id:
                # If the book is found, proceed with updating its information
                while True:
                    try:
                        # Call the function to prompt the user to update exisiting book
                        message = self.promptBookInfo(book)
                        # Return the message indicating the result of the update
                        return message
                    except ValueError as error:
                        # If any validation fails, catch the error and continue the loop
                        print(f"Error updating book: {error}\n")

        # If no book with the given ID is found, return a message indicating the book was not found
        return (f"Book ID: {id} was not found.\n")
    
    # Function to prompt the user to enter new information for a book and either create a new book or update an existing one
    def promptBookInfo(self, book=None):
        while True:
            try:
                # Prompt the user to enter new information for the book
                if book is None:
                    print("Enter the new information for a new Book:")
                else:
                    print(f"Enter the new information for the Book: {book.title}")
                
                # Validate and input the new title
                while True:
                    title = input("Enter new title: ")
                    if title and all(c.isalnum() or c in (" ", "'") for c in title):
                        break
                    print("Title cannot be empty and must contain only alphanumeric characters, spaces, or apostrophes.")

                # Validate and input the new author
                while True:
                    author = input("Enter new author: ")
                    if author and not any(char.isdigit() for char in author):
                        break
                    print("Author cannot be empty and must not contain any numbers.")

                # Validate and input the new price
                while True:
                    try:
                        price = float(input("Enter new price: "))
                        if price > 0:
                            break
                        print("Price must be positive.")
                    except ValueError:
                        print("Invalid price format. Please enter a valid price.")

                # Validate and input the new copyright date
                while True:
                    copyright_date = input("Enter new published date (Month-Day-Year): ")
                    if re.match(r'\d{2}-\d{2}-\d{4}', copyright_date):
                        # Extract day, month, and year from the date string
                        month, day, year = map(int, copyright_date.split('-'))

                        # Check if the month is between 1 and 12
                        if month < 1 or month > 12:
                            print("Invalid month. Month should be between 01 and 12.")
                            continue

                        # Check if the day is between 1 and 31 (depending on the month)
                        if day < 1 or (month in [1, 3, 5, 7, 8, 10, 12] and day > 31) or \
                        (month in [4, 6, 9, 11] and day > 30) or \
                        (month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and day > 29) or \
                        (month == 2 and ((year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)) and day > 28):
                            print("Invalid day. Day should be valid for the given month.")
                            continue

                        # Check if the year is between 1800 and 2025
                        if year < 1800 or year > 2025:
                            print("Invalid year. Year should be between 1800 and 2025.")
                            continue

                        # If all checks pass, break out of the loop
                        break
                    else:
                        print("Invalid date format. Use MM-DD-YYYY format.")

                if book is None:
                    # If the method is used for creating a new book
                    # generate a unique ISBN and create a new book object
                    isbn = self.generate_unique_isbn()
                    new_book = Books(len(self.Books_in_my_library) + 1, title, author, isbn, price, copyright_date)
                    self.Books_in_my_library.append(new_book)
                    self.existing_isbns.add(isbn)

                    # Return a success message
                    return "Book created successfully."
                else:
                    # If the method is used for updating an existing book,
                    # update the book's information and return a success message
                    book.title = title
                    book.author = author
                    book.price = price
                    book.copyright_date = copyright_date

                    # Return a message indicating the successful update of the book
                    return f"Book with ID {book.id} has been updated.\n"
            except ValueError as error:
                # If any validation fails, catch the error and continue the loop
                print(f"Error creating/updating book: {error}\n")

    # Function to generate a unique ISBN for the new book
    def generate_unique_isbn(self):
        while True:
            isbn = str(978) + str(random.randint(1000000000, 9999999999))
            if isbn not in self.existing_isbns:
                return isbn

    # Function to display the menu options
    def menu(self):
        print("1 Show all the books")
        print("2 Create a book")
        print("3 Remove a book")
        print("4 Find book(s) by string")
        print("5 Update a book")
        print("6 to quit")