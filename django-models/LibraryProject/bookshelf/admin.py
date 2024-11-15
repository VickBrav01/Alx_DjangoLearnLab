from django.contrib import admin
from .models import Book  # Import your Book model


# Register the model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Step 2 (Customize the admin list view below)
    list_display = ("title", "author", "publication_year")
    list_filter = ("author", "publication_year")
    search_fields = ("title", "author")
