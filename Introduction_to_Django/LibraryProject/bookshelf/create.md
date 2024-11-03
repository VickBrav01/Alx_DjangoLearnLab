from bookshelf.models import Book

<!-- Create a new book -->

new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

<!-- new_book.save() -->
