from django.shortcuts import render, get_object_or_404
from .models import Article
from django.core.paginator import Paginator


def all_articles(request):
    objects_list = Article.objects.order_by('-created_at')
    paginator = Paginator(objects_list, 6)
    page_num = request.GET.get('page')
    articles = paginator.get_page(page_num)
    return render(request, 'blog/all_articles.html', {'articles': articles})


def article_details(request, pk):
    article = get_object_or_404(Article, id=pk)
    recent_articles = Article.objects.order_by('-created_at')
    return render(request, 'blog/article_details.html', {'article': article, 'recent_articles': recent_articles})
