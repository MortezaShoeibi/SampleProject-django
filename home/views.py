from django.shortcuts import render
from .models import *


def home(request):
    foreword = Foreword.objects.last()
    about_me = AboutMe.objects.last()
    count_up = CountUp.objects.last()
    return render(request, 'home/index.html', {
        'foreword': foreword,
        'about_me': about_me,
        'count_up': count_up,
    })
