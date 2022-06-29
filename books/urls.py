from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('<int:pk>/book-details', views.book_details, name='book_details'),
]
