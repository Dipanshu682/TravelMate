from django.urls import path
from .views import (
    trip_preference,
    create_trip_preference,
    edit_trip_preference,
    home,
    explore,
    add_comment,
    delete_comment,
)

urlpatterns = [
    path("", home, name="home"),
    path("explore/", explore, name="explore"),
    path("trip-preference/", trip_preference, name="trip_preference"),
    path(
        "trip-preference/create/",
        create_trip_preference,
        name="create_trip_preference",
    ),
    path(
        "trip-preference/<int:pk>/edit/",
        edit_trip_preference,
        name="edit_trip_preference",
    ),
    path("<int:pk>/comment/", add_comment, name="add_comment"),
    path("comment/<int:pk>/delete/", delete_comment, name="delete_comment"),
]
