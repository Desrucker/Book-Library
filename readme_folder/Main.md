# Main.py

## Overview
This program manages a collection of books through various functionalities such as displaying, creating, removing, searching, and updating books.

## Libraries Used
- **colorama**: Used for colored text output.
- **Dataclass.BookShelf**: Importing `BookShelf` class from `Dataclass` module for managing books.

## Functions and Main Logic

### `displayAllBooks(book_shelf)`
- Displays all books in the bookshelf.

### `main()`
- The main function to run the program.
- Initializes a `BookShelf` object.
- Enters a loop to continuously prompt the user for input and execute corresponding actions based on menu options.
- Menu options are presented in cyan color.
- Handles various cases for different menu options:
  - Case 1: Display all books
  - Case 2: Create a new book
  - Case 3: Remove a book
  - Case 4: Display books containing a specific string
  - Case 5: Update book information
  - Case 6: Exit the program
- Handles invalid input gracefully.

## Running the Program
The program starts executing from the `main()` function. Run the script and follow the prompts to perform book management tasks.
