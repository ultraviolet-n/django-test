"""
URL configuration for hexlet_django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog import view
from .view import IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(template_name='index.html')),
    path('about/', view.about),
    path('article/', include('hexlet_django_blog.article.urls')),
    path('admin/', admin.site.urls),
]
