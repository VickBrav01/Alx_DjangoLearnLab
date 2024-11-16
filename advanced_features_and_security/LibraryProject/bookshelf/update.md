book_to_update = Book.objects.get(title='1984')
book_to_update.title = 'Nineteen Eighty-Four'
book_to_update.save()
print(Book.objects.get(id=book_to_update.id))
"book.title"
