from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ExampleForm
from .models import Book
from django.contrib.auth.decorators import permission_required
# Create your views here.


# Home Page
class HomeView(TemplateView):
    template_name = 'bookshelf/book_list.html'


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            return render(request, 'bookshelf/form_example.html')
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
