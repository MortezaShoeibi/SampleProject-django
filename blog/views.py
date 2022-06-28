from django.shortcuts import render, get_object_or_404
from .models import Article, Comment
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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(name=name, email=email, body=body, article=article, parent_id=parent_id)
    return render(request, 'blog/article_details.html', {'article': article, 'recent_articles': recent_articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    paginator = Paginator(articles, 6)
    page_num = request.GET.get('page')
    objects_list = paginator.get_page(page_num)
    return render(request, "blog/all_articles.html", {'articles': objects_list})
