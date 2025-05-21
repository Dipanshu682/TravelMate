import pytest
from django.contrib.auth.models import User
from profiles.models import Profile


@pytest.mark.django_db
def test_profile_creation():
    user = User.objects.create_user(username="testuser", password="A!s2d3f4g5h6")
    profile = Profile.objects.get(user=user)

    assert profile.user == user
    assert profile.name == ""
    assert profile.age == 18
    assert profile.get_full_name() == " "


@pytest.mark.django_db
def test_profile_str():
    user = User.objects.create_user(username="testuser", password="A!s2d3f4g5h6")
    profile = Profile.objects.get(user=user)

    assert str(profile) == "testuser"
