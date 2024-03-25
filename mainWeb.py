from flask import Flask, render_template, request, redirect, url_for
from werkzeug.exceptions import BadRequestKeyError
from Webclass import BookShelf

app = Flask(__name__)
data_source = BookShelf()

# Error handler for BadRequestKeyError
@app.errorhandler(BadRequestKeyError)
def handle_bad_request_error(e):
    return render_template('error.html', error_message="Bad Request: Required form field is missing."), 400

# Route to display all books
@app.route('/')
def index():
    # Display all books initially
    books = data_source.getAllBooks()
    return render_template('index.html', books=books)

# Route to search for books
@app.route('/search', methods=['POST'])
def search():
    try:
        search_query = request.form['search_query']
    except BadRequestKeyError:
        return render_template('error.html', error_message="Bad Request: Required form field is missing."), 400
    
    if search_query:
        books = data_source.searchBooks(search_query)
    else:
        books = data_source.getAllBooks()
    return render_template('index.html', books=books)

# Route to add a new book
@app.route('/new', methods=['POST'])
def new_book():
    if request.method == 'POST':
        # Check if the form is empty. If it is, redirect to the index page
        try:
            title = request.form['title']
            author = request.form['author']
            isbn = request.form['isbn']
            price = request.form['price']
            copyright_date = request.form['copyright_date']
        except BadRequestKeyError:
            return render_template('error.html', error_message="Bad Request: Required form field is missing."), 400
        
        # Validate form fields
        if not title.strip() or not author.strip() or not isbn.strip():
            error_message = "Title, author, and ISBN are required fields."
            return render_template('error.html', error_message=error_message), 400
        
        validation_result = data_source.validateBookInfo(title, author, isbn, price, copyright_date)
        if validation_result:
            return render_template('error.html', error_message=validation_result), 400

        # If the form is not empty and valid, create a new book and redirect to the index page
        data_source.createBook(title, author, isbn, price, copyright_date) 
        return redirect(url_for('index')) 
    
# Route to render the form for adding a new book
@app.route('/newForm')
def new_book_form():
    return render_template('new.html')

# Route to render the form for editing a book
@app.route('/editForm/<int:id>', methods=['GET'])   
def edit_book_form(id):
    book = data_source.findBook(id) 
    return render_template('edit.html', book=book)

# Route to edit a book
@app.route('/edit', methods=['POST'])
def edit_book_post():
    try:
        id = int(request.form['id'])
    except (ValueError, KeyError):
        return render_template('error.html', error_message="Invalid book ID provided."), 400
    
    # Retrieve form data
    title = request.form.get('title', '')
    author = request.form.get('author', '')
    isbn = request.form.get('isbn', '')
    price = request.form.get('price', '')
    copyright_date = request.form.get('copyright_date', '')

    # Validate form fields
    if not title.strip() or not author.strip() or not isbn.strip():
        error_message = "Title, author, and ISBN are required fields."
        return render_template('error.html', error_message=error_message), 400

    validation_result = data_source.validateBookInfo(title, author, isbn, price, copyright_date)
    if validation_result:
        return render_template('error.html', error_message=validation_result), 400

    # If validation successful, update the book and redirect to the index page
    data_source.updateBook(id, title, author, isbn, price, copyright_date)
    return redirect(url_for('index'))

# Route to delete a book
@app.route('/delete/<int:id>', methods=['GET'])
def delete_book(id):
    book = data_source.findBook(id)  # Retrieve the book to display its details
    return render_template('delete.html', book=book)

# Route to confirm and delete a book
@app.route('/confirm_delete/<int:id>', methods=['POST'])
def confirm_delete_book(id):
    data_source.removeBook(id) 
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
