from django.shortcuts import render
from .models import *
from blog.models import *
from books.models import *


def home(request):
    foreword = Foreword.objects.last()
    about_me = AboutMe.objects.last()
    count_up = CountUp.objects.last()
    target = Target.objects.last()
    books = Book.objects.order_by('-created_at')[:5]
    activities = CulturalActivity.objects.order_by('-title')
    articles = Article.objects.order_by('-created_at')
    video = Video.objects.last()
    return render(request, 'home/index.html', {
        'foreword': foreword,
        'about_me': about_me,
        'count_up': count_up,
        'target': target,
        'books': books,
        'activities': activities,
        'articles': articles,
        'video': video,
    })
