from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('all-articles', views.all_articles, name='all_articles'),
]

