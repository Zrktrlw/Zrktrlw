from django.shortcuts import render, HttpResponse
from .models import Article, articleCategory

def article_homepage_view(request):
    article = Article.objects.first()
    print(article.created_date)
    return render(request, "articles/articles.html")

def articles_category(request):
    makale = Article.objects.all()
    print(makale)
    return render(request, "articles/article-category.html")