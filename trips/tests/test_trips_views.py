import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from trips.models import TripPreference


@pytest.mark.django_db
def test_create_trip_preference_view(client):
    user = User.objects.create_user(username="testuser", password="A!s2d3f4g5h6")
    client.login(username="testuser", password="A!s2d3f4g5h6")
    url = reverse("create_trip_preference")
    response = client.post(url, {"destination": "Paris", "date": "2024-12-25"})
    assert response.status_code == 302
    assert TripPreference.objects.filter(destination="Paris").exists()


@pytest.mark.django_db
def test_trip_preference_view(client):
    user = User.objects.create_user(username="testuser", password="A!s2d3f4g5h6")
    TripPreference.objects.create(user=user, destination="Paris", date="2024-12-25")
    client.login(username="testuser", password="A!s2d3f4g5h6")
    url = reverse("trip_preference")
    response = client.get(url)
    assert response.status_code == 200
    assert "Paris" in response.content.decode()


@pytest.mark.django_db
def test_edit_trip_preference_view(client):
    user = User.objects.create_user(username="testuser", password="A!s2d3f4g5h6")
    trip_preference = TripPreference.objects.create(
        user=user, destination="Paris", date="2024-12-25"
    )
    client.login(username="testuser", password="A!s2d3f4g5h6")
    url = reverse("edit_trip_preference", kwargs={"pk": trip_preference.pk})
    response = client.post(url, {"destination": "London", "date": "2024-12-25"})
    assert response.status_code == 302
    trip_preference.refresh_from_db()
    assert trip_preference.destination == "London"
