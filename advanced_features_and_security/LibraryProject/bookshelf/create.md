first_book = Book(title = '1984', author = "George Orwell", publication_year = 1949)
Book.objects.create
first_book.save()
#new book creation
