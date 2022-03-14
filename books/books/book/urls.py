from django.urls import path
from .views import index, book_details, add_book

app_name = "fav_books"

urlpatterns = [
    path('', index, name='book_index'),
    path('<int:book_id>', book_details, name='book_detail'),
    path('add_book', add_book, name='add_book')
]
