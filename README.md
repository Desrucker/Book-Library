# Book Management System

## Introduction
This program is a book management system that allows users to perform various operations such as adding, removing, updating, and searching for books in a library. It provides a user-friendly interface with a menu-driven approach.

## Functionality
The program offers the following functionalities:
- Display all books in the library.
- Create a new book.
- Remove an existing book.
- Find book(s) by title, author, or copyright date.
- Update information of an existing book.

## Components

### `main.py`
- **Description**: This script contains the main program logic, including the menu-driven interface.
- **Functionality**: It interacts with the user, displays menu options, and calls corresponding functions based on user input.

### `BookShelf.py`
- **Description**: This module defines the `BookShelf` class responsible for managing the collection of books.
- **Functionality**: It provides methods for loading, saving, adding, removing, updating, and searching books in the library.

### `Book.py`
- **Description**: This module defines the `Books` class, representing individual book objects.
- **Functionality**: It stores attributes such as ID, title, author, ISBN, price, and copyright date of each book.

### `colorama` and `re` Libraries
- **Description**: These libraries are used for colored text output and regular expression matching, respectively.
- **Functionality**: `colorama` adds visual appeal to the program by allowing colored text output, while `re` is used for validating date formats.

## Usage
1. Run the `main.py` script.
2. Follow the on-screen instructions to navigate through the menu options and perform desired operations.
3. Interact with the program until you are finished, and exit by choosing the appropriate option from the menu.

## Dependencies
- Python 3.10+
- `colorama` library
