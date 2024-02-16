class Books:

	def __init__(self, id, title, author, isbn, price, copyright_date):
		self.id = id
		self.title = title
		self.author = author
		self.isbn = isbn
		self.price = price 
		self.copyright_date = copyright_date

	def __str__(self):
		return f"Book ID: {self.id}, Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: {self.price}, Copyright Date: {self.copyright_date}"
