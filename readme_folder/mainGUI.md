# Book Management GUI

This Python script creates a graphical user interface (GUI) for managing a collection of books. It uses PySimpleGUI library to build the interface.

## Main Features

- **Show All Books**: Displays all books currently in the collection.
- **Search Books**: Allows users to search for books by title, author, or other criteria.
- **Add/Edit Books**: Provides forms for adding new books or editing existing ones.
- **Delete Books**: Allows users to remove books from the collection.

## Code Overview

### `MainGUI` Class

- `__init__(self)`: Initializes the GUI and sets up the layout.
- `run(self)`: Runs the GUI event loop, handling user interactions and updating the display accordingly.

### Event Handling Methods

- `show_books(self, books)`: Updates the book table with new values.
- `make_rows(self, books)`: Creates rows for the book table based on the provided list of books.
- `show_add_edit_form(self, book=None, update=False)`: Displays a form for adding or editing a book.
- `setup_layout(self)`: Sets up the layout of the GUI, including search input, book table, and control buttons.

### Other Components

- `BookShelf`: A data class or module that manages the collection of books.
- Various button actions such as show all, search, add, edit, and delete, each associated with specific events and corresponding actions.

## How to Run

- Make sure you have Python installed on your system.
- Install PySimpleGUI library if not already installed (`pip3 install PySimpleGUI==4.60.5`).
- Run the script, and the GUI for managing books will appear.

