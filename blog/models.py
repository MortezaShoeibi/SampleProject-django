from django.db import models
from django.urls import reverse
from tinymce import models as tiny_models


class Article(models.Model):
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر')
    title = models.CharField(max_length=50, verbose_name='تیتر')
    body = tiny_models.HTMLField(verbose_name='متن')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    def __str__(self):
        return f'-{self.title}'

    def get_absolute_url(self):
        return reverse('blog:article_details', args=[self.id])

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'مقالات'
        verbose_name_plural = 'مقاله'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله')
    name = models.CharField(max_length=100, verbose_name='نام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    body = models.TextField(verbose_name='متن')
    email = models.EmailField(verbose_name='ایمیل')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True, verbose_name='کامنت والد')

    def __str__(self):
        return f'{self.name}: {self.body[:15]}...'

    class Meta:
        verbose_name = 'نظرات'
        verbose_name_plural = 'نظر'
