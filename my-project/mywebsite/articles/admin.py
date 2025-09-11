from django.contrib import admin
from .models import Article, articleCategory,articleUser

admin.site.register(Article)
admin.site.register(articleCategory)
admin.site.register(articleUser)
