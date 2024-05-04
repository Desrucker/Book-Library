# Book Management System

## Introduction
The Book Management System is a web-based application designed to streamline library operations by providing a user-friendly interface for managing books. Users can easily perform various tasks such as adding, removing, updating, and searching for books within the library.

## Functionality
The program offers the following key functionalities:
- Display all books in the library.
- Create a new book entry.
- Remove an existing book from the collection.
- Search for books by title, author, or copyright date.
- Update information for existing books.

## Components

### `main.py`
- **Description**: This script serves as the main entry point for the program, implementing the web interface.
- **Functionality**: It handles HTTP requests, presents web pages, and executes corresponding functions based on user interactions.

### `BookShelf.py`
- **Description**: The `BookShelf` class defined in this module manages the library's collection of books.
- **Functionality**: It provides methods for loading, saving, adding, removing, updating, and searching for books in the library.

### `Book.py`
- **Description**: This module defines the `Book` class, representing individual book objects.
- **Functionality**: It encapsulates attributes such as ID, title, author, ISBN, price, and copyright date for each book.

### `colorama` and `re` Libraries
- **Description**: These libraries enhance the program's functionality by enabling colored text output and regular expression matching, respectively.
- **Functionality**: `colorama` adds visual appeal to the interface, while `re` aids in validating date formats.

## Usage
1. Run the `main.py` script using Python 3.10 or above.
2. Open your web browser and navigate to the provided URL (usually `http://localhost:5000`).
3. Use the web interface to perform various tasks like adding, updating, or removing books.

## Dependencies
- Python 3.10+
- `colorama` library

## Future Enhancements (Potential)
1. **User Authentication**: Implement user authentication and access control features to allow multiple users with different privileges to interact with the system.
2. **User Reviews and Ratings**: Introduce a feature where users can leave reviews and ratings for books they have read. This social aspect could foster community interaction and help other users make informed decisions about which books to read.
