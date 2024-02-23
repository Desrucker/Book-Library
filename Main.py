import colorama  # Import colorama library for colored text
from Dataclass import BookShelf  # Import BookShelf class from Dataclass module

def displayAllBooks(book_shelf):
    """Display all books in the bookshelf."""
    books = book_shelf.getAllBooks()
    for book in books:
        print(book)

def main():
    """Main function to run the program."""
    # Initialize BookShelf object
    book_shelf = BookShelf()

    while True:
        # Print menu options in cyan color
        print(colorama.Fore.CYAN)
        book_shelf.menu()
        print(colorama.Style.RESET_ALL)
        try:
            # Get user input for menu option
            response = int(input("Enter a number: "))
            print()
            
            # Use match statement for handling menu options
            match response: 
                case 1: # Case 1: Display all books
                    displayAllBooks(book_shelf)

                case 2: # Case 2: Create a new book
                    print("You have selected to create a new book.\n")
                    message = book_shelf.createBook()
                    print(message)

                case 3: # Case 3: Remove a book
                    print("You have selected to remove a book.\n")
                    displayAllBooks(book_shelf)
                    result = book_shelf.removeBook()
                    print(f"{result}\n") if result else print(f"Book with the specified ID was not found.\n")

                case 4: # Case 4: Display books containing a string
                    search_string = input("Enter string to search: ")
                    found_books = book_shelf.searchBooks(search_string)
                    [print(book) for book in found_books] or print("No matching books found\n")

                case 5: # Case 5: Update information 
                    print("You have selected to update book information.\n")
                    displayAllBooks(book_shelf)
                    message = book_shelf.updateBookById()
                    print(f"{message}\n")

                case 6: # Case 6: Exit the program
                    print("Exiting Program")
                    break
                
                case _: # Handle invalid input
                    print("Invalid number. Please enter a valid option.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

if __name__ == '__main__':
    main()
