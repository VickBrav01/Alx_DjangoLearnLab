<!-- Retrieve all books from the database -->

books = Book.objects.all()

for book in books:
    print(book)
