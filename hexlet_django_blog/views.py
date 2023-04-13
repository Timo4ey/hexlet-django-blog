from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect


class ViewIndex(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*kwargs)
        context['who'] = 'World'
        return context
    

    def get(self, request, *args, **kwargs):
        request.
        redirect_url = reverse('article', kwargs={'tag': 'python', 'id': 42})
        return HttpResponseRedirect(redirect_url)

        # return redirect('article', tag='python', id=42)



def about(request):
    return render(request, 'about.html')

