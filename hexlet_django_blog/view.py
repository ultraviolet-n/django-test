from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):
    template_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


def about(request):
    return render(request, 'about.html')
