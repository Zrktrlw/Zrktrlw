from django.urls import path
from .views import user_homepage_view

urlpatterns = [
    path("my-profile/", user_homepage_view, name="my-profile-homepage"),
]
