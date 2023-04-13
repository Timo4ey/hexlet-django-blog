from django.urls import path, re_path

# from hexlet_django_blog.article import views
from .views import Article


urlpatterns = [
        path('', Article.as_view()),
        path('<str:tag>/<int:id>/', Article.as_view(), name='article'),
        # re_path('^article/(?P<tag>[^/]+)/(?P<id>[0-9]+)/\\Z', )
        ]
