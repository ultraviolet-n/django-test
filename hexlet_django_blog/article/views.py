from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

from django.views import View


class IndexView(View):

    def get(self, request, tags, article_id):
        return redirect(reverse('article', kwargs={'article_id': article_id, 'tags': tags}))


def index(request, tags, article_id):
    return render(request, 'article/index.html', context={'tags': tags, 'article_id': article_id})
