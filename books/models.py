from django.db import models
from django.urls import reverse
from tinymce import models as tiny_models


class Book(models.Model):
    image = models.ImageField(upload_to='books/images')
    title = models.CharField(max_length=50)
    body = tiny_models.HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'-{self.title}'

    def get_absolute_url(self):
        pass
        return reverse('books:book_details', args=[self.id])

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب'


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    email = models.EmailField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)

    def __str__(self):
        return f'{self.name}: {self.body[:15]}...'

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
