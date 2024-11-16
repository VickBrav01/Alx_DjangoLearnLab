book_to_delete = Book.objects.get(title='Nineteen Eighty-Four')
book_to_delete.delete()
print(Book.objects.all())
"book.delete", "from bookshelf.models import Book"
