from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator


def all_books(request):
    objects_list = Book.objects.order_by('-created_at')
    paginator = Paginator(objects_list, 3)
    page_num = request.GET.get('page')
    books = paginator.get_page(page_num)
    return render(request, 'books/all_books.html', {'books': books})


def book_details(request, pk):
    book = get_object_or_404(Book, id=pk)
    recent_books = Book.objects.order_by('-created_at')
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(name=name, email=email, body=body, book=book, parent_id=parent_id)
    return render(request, 'books/book_details.html', {'book': book, 'recent_books': recent_books})
