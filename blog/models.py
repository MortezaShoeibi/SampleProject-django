from django.db import models
from django.urls import reverse


class Article(models.Model):
    image = models.ImageField(upload_to='articles/images')
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'-{self.title}'

    def get_absolute_url(self):
        return reverse('blog:article_details', args=[self.id])

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله'
