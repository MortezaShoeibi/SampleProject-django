from django.db import models
from django.urls import reverse
from tinymce import models as tiny_models


class Book(models.Model):
    image = models.ImageField(upload_to='images/books', verbose_name='تصویر')
    title = models.CharField(max_length=50, verbose_name='تیتر')
    body = tiny_models.HTMLField(verbose_name='متن')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    def __str__(self) -> str:
        return f'-{self.title}'

    def get_absolute_url(self) -> str:
        return reverse('books:book_details', args=[self.id])

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'کتاب ها'
        verbose_name_plural = 'کتاب'


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', verbose_name='کتاب')
    name = models.CharField(max_length=100, verbose_name='نام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    body = models.TextField(verbose_name='متن')
    email = models.EmailField(verbose_name='ایمیل')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True, verbose_name='کامنت والد')

    def __str__(self) -> str:
        return f'{self.name}: {self.body[:15]}...'

    class Meta:
        verbose_name = 'نظرات'
        verbose_name_plural = 'نظر'
