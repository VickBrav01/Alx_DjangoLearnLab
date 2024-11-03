<!-- Delete a book with title (Brav) -->

delete_book = Book.objects.get(title="Pirates Of The Carebean")
delete_book.delete()
