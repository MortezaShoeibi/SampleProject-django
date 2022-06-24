from django.shortcuts import render
from .models import Article
from django.core.paginator import Paginator


def all_articles(request):
    objects_list = Article.objects.order_by('-created_at')
    paginator = Paginator(objects_list, 6)
    page_num = request.GET.get('page')
    articles = paginator.get_page(page_num)
    return render(request, 'blog/all_articles.html', {'articles': articles})

