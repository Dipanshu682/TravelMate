from django.urls import path
from .views import profile, edit_profile

urlpatterns = [
    path("edit/", edit_profile, name="edit_profile"),
    path("<str:username>/", profile, name="profile"),
]
