from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

TEAM = [
    {'name': 'Yoda', 'position': 'CEO'},
    {'name': 'Obi-Wan Kenobi', 'position': 'Senior Developer'},
    {'name': 'Anakin Skywalker', 'position': 'Junior Developer'},
    {'name': 'Jar Jar Binks', 'position': 'Trainee'},
]


def index(request):
    return HttpResponse('article')


def article(request):
    return render(request, 'article.html', context={'TEAM': TEAM})
