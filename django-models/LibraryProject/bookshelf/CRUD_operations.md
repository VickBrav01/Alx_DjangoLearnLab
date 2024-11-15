> > > from bookshelf.models import Book

<!-- Create a new book -->

> > > new_book = Book(title="1984", author="George Orwell", publication_year=1949)
> > >
> > > new_book.save()

<!-- Retrieve Books -->

> > > books = Book.objects.all()
> > >
> > > for book in books:
> > > ... print(book)
> > > ...
> > > Name: Pirates Of The Carebean Author: Jack Sparrow  
> > > Name: 1984 Author: George Orwell

<!-- Update Title to Nineteen Eighty-Four -->

> > > update_book = Book.objects.filter(title="1984").update(title="Nineteen Eighty-Four")

<!-- Delete a book from the store -->

> > > delete_book = Book.objects.get(title="Pirates Of The Carebean")
> > > delete_book.delete()
> > > (1, {'bookshelf.Book': 1})
