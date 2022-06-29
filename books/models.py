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
        # return reverse('books:book_details', args=[self.id])

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب'
