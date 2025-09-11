from django.shortcuts import render, HttpResponse
from articles.models import Article

def user_homepage_view(request):
    articles = Article.objects.all()
    first_name = request.user.first_name
    ctx = {
        "first_name": first_name,
        "articles": articles
    }
    return render(request, "user-list/user-profile.html",ctx)


# Create your views here.
