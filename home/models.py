from django.db import models


class Foreword(models.Model):
    image = models.ImageField(upload_to='images/welcome', verbose_name='تصویر')
    name = models.CharField(max_length=200, verbose_name='نام')
    welcome = models.CharField(max_length=400, verbose_name='متن خوش آمد گویی')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return self.welcome

    class Meta:
        verbose_name = 'معرفی'
        verbose_name_plural = 'معرفی'


class AboutMe(models.Model):
    image = models.ImageField(upload_to='images/about_me', verbose_name='تصویر')
    question = models.CharField(max_length=80, verbose_name='سوال')
    text = models.TextField(verbose_name='متن')

    def __str__(self):
        return f'{self.question}: -{self.text[:10]}...'

    class Meta:
        verbose_name = 'درباره من'
        verbose_name_plural = 'درباره من'


class CountUp(models.Model):
    published = models.CharField(max_length=5000, verbose_name='کتاب های منتشر شده')
    being_printed = models.CharField(max_length=5000, verbose_name='کتاب های در دست چاپ')
    sold_volume = models.CharField(max_length=5000, verbose_name='جلدهای فروخته شده')
    idea = models.CharField(max_length=5000, verbose_name='ایده های کار نشده')

    def __str__(self):
        return f'منتشر شده: {self.published}'

    class Meta:
        verbose_name = 'شمارشگر'
        verbose_name_plural = 'شمارشگر'


class Target(models.Model):
    question = models.CharField(max_length=100, verbose_name='سوال')
    title = models.CharField(max_length=100, verbose_name='تیتر')
    text = models.TextField(verbose_name='متن')

    def __str__(self):
        return f'{self.question} -{self.title[:10]}...'

    class Meta:
        verbose_name = 'هدف'
        verbose_name_plural = 'هدف'


class CulturalActivity(models.Model):
    title = models.CharField(max_length=150, verbose_name='تیتر')
    activity = models.TextField(verbose_name='فعالیت')
    image = models.ImageField(upload_to='images/cultural', null=True, blank=True, verbose_name='تصویر')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('-title',)
        verbose_name = 'فعالیت های فرهنگی'
        verbose_name_plural = 'فعالیت های فرهنگی'


class Video(models.Model):
    title = models.CharField(max_length=100, verbose_name='تیتر')
    image = models.ImageField(upload_to='images/Video', verbose_name='تصویر')
    url = models.URLField(verbose_name='لینک')
    description = models.TextField(verbose_name='توضیحات')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'ویدیو'
        verbose_name_plural = 'ویدیو'


class ContactUs(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    text = models.TextField(verbose_name='متن')
    email = models.EmailField(verbose_name='ایمیل')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    def __str__(self):
        return f' شما یک پیام از طرف {self.name} دارید '

    class Meta:
        verbose_name = 'پیام ها'
        verbose_name_plural = 'پیام'


class Social(models.Model):
    title = models.CharField(max_length=250, primary_key=True, verbose_name='نام شبکه اجتماعی')
    url = models.URLField(max_length=1000, verbose_name='لینک')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'شبکه های اجتماعی'
        verbose_name_plural = 'شبکه اجتماعی'
