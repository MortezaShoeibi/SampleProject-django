from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('all-books', views.all_books, name='all_books'),
    path('<int:pk>/book-details', views.book_details, name='book_details'),
    path('search/', views.search, name='search'),
]
