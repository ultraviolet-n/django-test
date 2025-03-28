from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import View

TEAM = [
    {'name': 'Yoda', 'position': 'CEO'},
    {'name': 'Obi-Wan Kenobi', 'position': 'Senior Developer'},
    {'name': 'Anakin Skywalker', 'position': 'Junior Developer'},
    {'name': 'Jar Jar Binks', 'position': 'Trainee'},
]


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Article')


def article(request):
    return render(request, 'article.html', context={'TEAM': TEAM})
