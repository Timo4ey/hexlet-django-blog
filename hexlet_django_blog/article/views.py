from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Article(View):
    template_name = 'article.html'

    def get(self, *args, **kwargs):
        return render(*args, self.template_name, context={
        'name': 'Article'})
