from django.db import models


class Foreword(models.Model):
    image = models.ImageField(upload_to='welcome/images')
    name = models.CharField(max_length=200)
    welcome = models.CharField(max_length=400)
    description = models.TextField()

    def __str__(self):
        return self.welcome

    class Meta:
        verbose_name = 'پیشگفتار'
        verbose_name_plural = 'پیشگفتار'


