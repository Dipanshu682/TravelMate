import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_view(client):
    user = User.objects.create_user(username="testuser", password="A!s2d3f4g5h6")
    profile = Profile.objects.get(user=user)
    profile.name = "John Doe"
    profile.save()

    response = client.get(f"/profile/{user.username}/")
    assert response.status_code == 200
    assert "John Doe" in response.content.decode()


@pytest.mark.django_db
def test_edit_profile_view(client):
    user = User.objects.create_user(username="testuser", password="A!s2d3f4g5h6")
    profile = Profile.objects.get(user=user)
    profile.name = "John Doe"
    profile.save()

    client.login(username="testuser", password="A!s2d3f4g5h6")
    response = client.post(
        "/profile/edit/",
        {
            "name": "Jane Doe",
            "age": 25,
            "gender": "Female",
        },
    )

    assert response.status_code == 302
    profile.refresh_from_db()
    assert profile.name == "Jane Doe"
    assert profile.age == 25
    assert profile.gender == "Female"
