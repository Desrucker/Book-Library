import PySimpleGUI as myGUI  # Import PySimpleGUI library
from Dataclass import BookShelf  # Import the BookShelf class from Dataclass module

class MainGUI:
    def __init__(self):
        # Initialize the MainGUI class
        self.book_shelf = BookShelf()  # Initialize BookShelf instance
        self.books = []  # Initialize an empty list for books
        self.setupLayout()  # Call the setupLayout method to set up the GUI

    def run(self):
        # Run the GUI event loop
        while True:
            # Read events and values from the window
            event, values = self.window.read()
            # Check if the window is closed or exit button is clicked
            if event == myGUI.WINDOW_CLOSED or event == 'EXIT_BUTTON':
                break
            # Show all books in the book table
            elif event == 'SHOW_ALL':
                self.showBooks(self.book_shelf.getAllBooks())
            # Search for books based on user input
            elif event == 'SEARCH_BUTTON':
                search_query = values['SEARCH_INPUT']
                if search_query == '':
                    self.showBooks(self.book_shelf.getAllBooks())
                else:
                    self.showBooks(self.book_shelf.searchBooks(search_query))
            # Show form for adding a new book
            elif event == 'NEW_BUTTON':
                self.showAddEditForm()
            # Show form for editing a selected book
            elif event == 'EDIT_BUTTON':
                selected_row = values['BOOK_TABLE'][0] if values['BOOK_TABLE'] else None
                if selected_row is not None:
                    book_id = self.window['BOOK_TABLE'].get()[selected_row][0]
                    book = self.book_shelf.findBook(int(book_id))
                    self.showAddEditForm(book, update=True)
            # Delete a selected book
            elif event == 'DELETE_BUTTON':
                selected_row = values['BOOK_TABLE'][0] if values['BOOK_TABLE'] else None
                if selected_row is not None:
                    book_id = self.window['BOOK_TABLE'].get()[selected_row][0]
                    success = self.book_shelf.removeBook(int(book_id))
                    if not success:
                        myGUI.popup_error("Failed to delete the book.")
                    self.showBooks(self.book_shelf.getAllBooks())

        # Close the GUI window
        self.window.close()

    def showBooks(self, books):
        # Update the book table with new values
        self.window['BOOK_TABLE'].update(values=self.makeRows(books))

    def makeRows(self, books):
        # Create rows for the book table
        return [[book.id, book.title, book.author, book.isbn, f"{book.price:.2f}", book.copyright_date] for book in books]

    def showAddEditForm(self, book=None, update=False):
        # Show form for adding or editing a book
        title = book.title if book else ''
        author = book.author if book else ''
        price = str(book.price) if book else ''
        copyright_date = str(book.copyright_date) if book else ''

        layout = [
            [myGUI.Text("Title", size=(13, 1)), myGUI.InputText(default_text=title, key='TITLE')],
            [myGUI.Text("Author", size=(13, 1)), myGUI.InputText(default_text=author, key='AUTHOR')],
            [myGUI.Text("Price", size=(13, 1)), myGUI.InputText(default_text=price, key='PRICE')],
            [myGUI.Text("Copyright Date", size=(13, 1)), myGUI.InputText(default_text=copyright_date, key='COPYRIGHT_DATE')],
            [myGUI.Button("Submit", key='SUBMIT'), myGUI.Button("Cancel", key='CANCEL')]
        ]

        window = myGUI.Window("Edit Book" if book else "New Book", layout, finalize=True,)

        while True:
            event, values = window.read()
            if event in (myGUI.WINDOW_CLOSED, 'CANCEL'):
                break
            elif event == 'SUBMIT':
                if update:
                    book.title = values['TITLE']
                    book.author = values['AUTHOR']
                    book.price = values['PRICE']
                    book.copyright_date = values.get('COPYRIGHT_DATE', '')
                    book_info = (book.title, book.author, book.price, book.copyright_date)
                    validation_result = self.book_shelf.validateBookInfo(*book_info)
                    if isinstance(validation_result, list):
                        myGUI.popup('\n'.join(validation_result), title='Error')
                    else:
                        if validation_result == "Validation successful.":
                            self.book_shelf.saveBooks()
                            myGUI.popup("Book updated successfully.")
                        else:
                            myGUI.popup_error("Failed to update the book.")
                else:
                    title = values.get('TITLE', '')
                    author = values.get('AUTHOR', '')
                    price = values.get('PRICE', '')
                    copyright_date = values.get('COPYRIGHT_DATE', '')
                    book_info = (title, author, price, copyright_date)
                    validation_result = self.book_shelf.validateBookInfo(*book_info)
                    if isinstance(validation_result, list):
                        myGUI.popup('\n'.join(validation_result), title='Error')
                    else:
                        success = self.book_shelf.createBook(book_info)
                        if not success:
                            myGUI.popup_error("Failed to create the book.")
                self.showBooks(self.book_shelf.getAllBooks())
                break

        window.close()

    def setupLayout(self):
        # Set up the layout of the GUI
        search_layout = [
            [myGUI.Text("Search:"), myGUI.InputText(key='SEARCH_INPUT'), myGUI.Button("Search", key='SEARCH_BUTTON'), 
             myGUI.Button("Show All", key='SHOW_ALL'), myGUI.Button("New", key='NEW_BUTTON')]
        ]

        table_layout = [
            [myGUI.Table(headings=['ID', 'Title', 'Author', 'Isbn', 'Price', 'Copyright Date'], 
                      values=[], key='BOOK_TABLE', auto_size_columns=False, 
                      col_widths=[5, 30, 15, 12, 7, 13], enable_events=True, 
                      select_mode=myGUI.TABLE_SELECT_MODE_BROWSE)]
        ]

        button_layout = [
            [myGUI.Button("Edit", key='EDIT_BUTTON'), myGUI.Button("Delete", key='DELETE_BUTTON'), 
             myGUI.Button("Exit", key='EXIT_BUTTON', button_color=('white', 'red'))]
        ]

        self.layout = [
            search_layout,
            table_layout,
            button_layout
        ]

        self.window = myGUI.Window("Book Management", self.layout, finalize=True)

if __name__ == "__main__":
    app = MainGUI()
    app.run()
