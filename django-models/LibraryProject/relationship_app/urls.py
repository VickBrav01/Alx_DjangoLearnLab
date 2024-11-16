from .views import SpecificLibraryView, list_books
from django.urls import path

urlpatterns = [
    path('booklist/', view=list_books, name = 'listbooks'),
    path('library<id>',SpecificLibraryView.as_view(), name = 'library' )
]
