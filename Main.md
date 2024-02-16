The following Python code demonstrates a program for managing a bookshelf using a `BookShelf` data class.

### Importing Modules and Classes
- **Import Statement:** Importing the necessary modules and classes from `Dataclass.py`, including the `BookShelf` class.

### Functions
1. **`displayAllBooks(data_class)`:**
   - Displays all books present in the bookshelf by calling the `getAllBooks()` method of the `data_class`.

2. **`main()`:**
   - Entry point of the program.
   - Creates an instance of the `BookShelf` class.
   - Displays a menu of options and handles user input in a loop until the user chooses to exit.
     - Displays all books, creates a new book, removes a book, searches for books containing a string, updates information of a book, or exits the program based on user input.

### Execution
- The `main()` function is executed if the script is run directly.

### Usage
- Users can interact with the bookshelf by choosing from various menu options, such as displaying all books, adding a new book, removing a book, searching for books, updating book information, or exiting the program.

### Note
- Error handling is implemented to handle invalid user inputs, such as non-numeric input or invalid menu choices.
