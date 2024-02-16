# Import necessary modules and classes
from Dataclass import BookShelf

# Function to display all books in the bookshelf
def displayAllBooks(book_shelf):
    # Get all books from the bookshelf
    books = book_shelf.getAllBooks()
    # Print information for each book
    for book in books:
        print(book)
    print()

# Main function to interact with the bookshelf
def main():
    # Create an instance of the BookShelf class
    book_shelf = BookShelf()

    # Loop to display menu options and handle user input
    while True:
        # Display the menu
        book_shelf.menu()

        # Prompt the user to enter a number corresponding to their choice
        try:
            response = int(input("\nEnter a number: "))
            print()
            
            # Use a match statement to execute different actions based on user input
            match response: 
                # Case 1: Display all books
                case 1:
                    displayAllBooks(book_shelf)

                # Case 2: Create a new book
                case 2:
                    # Call the createBook method to add the new book to the bookshelf
                    message = book_shelf.createBook()
                    print(f"{message}\n")

                # Case 3: Remove a book
                case 3:
                    # Display all books in the bookshelf
                    displayAllBooks(book_shelf)
                    # Prompt the user to enter the ID of the book they want to remove
                    id = int(input("What book would you like to remove (Enter ID): "))
                    # Call the removeBook method to remove the specified book
                    result = book_shelf.removeBook(id)
                    # Print the result of the removal operation
                    if result is not None:
                        print(f"{result}\n")
                    else:
                        print(f"Book ID: {id} was not found.\n")

                # Case 4: Display books containing a string
                case 4:
                    search_string = input("Enter string to search: ")
                    found_books = book_shelf.searchBooks(search_string)
                    if found_books:
                        for book in found_books:
                            print(book)
                        print()
                    else:
                        print("No matching books found\n")

                # Case 5: Update information of a book
                case 5:
                    # Display all books in the bookshelf
                    displayAllBooks(book_shelf)
                    # Prompt the user to enter the ID of the book they want to update
                    id_to_update = int(input("What book would you like to update (Enter ID): "))
                    # Call the updateBook method to update the information of the specified book
                    message = book_shelf.updateBookById(id_to_update)
                    print(f"{message}\n")

                # Case 6: Exit the program
                case 6:
                    print("Exiting Program")
                    break
                
                # Default case: Selected option is not within options
                case _:
                    print("Invalid number. Please enter a valid option.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

# Entry point of the program
if __name__ == '__main__':
    main()
