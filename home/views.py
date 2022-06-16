from django.shortcuts import render
from .models import *


def home(request):
    foreword = Foreword.objects.last()
    return render(request, 'home/index.html', {'foreword': foreword})
