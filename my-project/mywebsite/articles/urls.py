from django.urls import path
from .views import article_homepage_view, articles_category

urlpatterns = [
    path("", article_homepage_view, name="article-homepage"),
    path("bilim/", articles_category),
]

