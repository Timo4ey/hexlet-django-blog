from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View


class Article(View):
    template_name = 'article.html'

    def get(self, *args, **kwargs):
        if kwargs.get('tag') and kwargs.get('id'):
            return HttpResponse(f'<h1>Статья номер {kwargs.get("id")}</h1><p>Тег {kwargs.get("tag")}</p>')
        return render(*args, self.template_name, context={
        'name': 'Article'})
    
