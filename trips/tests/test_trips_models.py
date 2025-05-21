import pytest
from django.contrib.auth.models import User
from trips.models import TripPreference, Comment


@pytest.mark.django_db
def test_trip_preference_str():
    user = User.objects.create_user(username="testuser", password="A!s2d3f4g5h6")
    trip_preference = TripPreference.objects.create(
        user=user, destination="Paris", date="2024-12-25"
    )
    assert str(trip_preference) == "testuser - Paris on 2024-12-25"


@pytest.mark.django_db
def test_comment_str():
    user = User.objects.create_user(username="testuser", password="A!s2d3f4g5h6")
    trip_preference = TripPreference.objects.create(
        user=user, destination="Paris", date="2024-12-25"
    )
    comment = Comment.objects.create(
        user=user, trip=trip_preference, text="Great trip!"
    )
    assert str(comment) == "Review for Paris by testuser"
