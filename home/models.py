from django.db import models


class Foreword(models.Model):
    image = models.ImageField(upload_to='welcome/images')
    name = models.CharField(max_length=200)
    welcome = models.CharField(max_length=400)
    description = models.TextField()

    def __str__(self):
        return self.welcome

    class Meta:
        verbose_name = 'خانه'
        verbose_name_plural = 'خانه'


class AboutMe(models.Model):
    image = models.ImageField(upload_to='about_me/images')
    question = models.CharField(max_length=80)
    text = models.TextField()

    def __str__(self):
        return f'{self.question}: -{self.text[:10]}...'

    class Meta:
        verbose_name = 'درباره من'
        verbose_name_plural = 'درباره من'


class CountUp(models.Model):
    published = models.CharField(max_length=5000)
    being_printed = models.CharField(max_length=5000)
    sold_volume = models.CharField(max_length=5000)
    idea = models.CharField(max_length=5000)

    def __str__(self):
        return f'published: {self.published}'

    class Meta:
        verbose_name = 'شمارشگر'
        verbose_name_plural = 'شمارشگر'


class Target(models.Model):
    question = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f'{self.question} -{self.title[:10]}...'

    class Meta:
        verbose_name = 'هدف'
        verbose_name_plural = 'هدف'
