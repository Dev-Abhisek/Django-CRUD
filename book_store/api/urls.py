from django.urls import path, include
from book_store.api.views import get_books, get_book


urlpatterns = [
    path('book_list/',get_books, name='Book-list'),
    path('book/<int:pk>/',get_book, name='Book-detail')
]
