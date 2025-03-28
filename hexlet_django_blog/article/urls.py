from django.urls import path
from hexlet_django_blog.article import views
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('article/', views.article),
]
