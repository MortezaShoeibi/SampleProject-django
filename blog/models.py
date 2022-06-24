from django.db import models


class Article(models.Model):
    image = models.ImageField(upload_to='articles/images')
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'-{self.title}'

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله'
