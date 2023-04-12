from django.urls import path

# from hexlet_django_blog.article import views
from .views import Article


urlpatterns = [
        path('', Article.as_view()),
        ]
