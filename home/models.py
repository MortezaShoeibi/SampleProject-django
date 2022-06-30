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


class CulturalActivity(models.Model):
    title = models.CharField(max_length=150)
    activity = models.TextField()
    image = models.ImageField(upload_to='cultural/images', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('-title',)
        verbose_name = 'فعلیت های فرهنگی'
        verbose_name_plural = 'فعالیت های فرهنگی'


class Video(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/Video')
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'ویدیو'
        verbose_name_plural = 'ویدیو'


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' شما یک پیام از طرف {self.name} دارید '

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class Social(models.Model):
    title = models.CharField(max_length=250, primary_key=True)
    url = models.URLField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'شبکه های اجتماعی'
        verbose_name_plural = 'شبکه های اجتماعی'
