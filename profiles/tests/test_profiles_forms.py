# profiles/tests/test_forms.py
import pytest
from profiles.forms import ProfileForm
from profiles.models import Profile
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_profile_form_valid_data():
    user = User.objects.create_user(username="testuser", password="A!s2d3f4g5h6")
    profile = Profile.objects.get(user=user)
    form = ProfileForm(
        data={
            "name": "John Doe",
            "age": 30,
            "gender": "Male",
            "bio": "A short bio",
            "location": "New York",
        },
        instance=profile,
    )

    assert form.is_valid()
    updated_profile = form.save()
    assert updated_profile.name == "John Doe"
    assert updated_profile.age == 30
    assert updated_profile.gender == "Male"
    assert updated_profile.bio == "A short bio"
    assert updated_profile.location == "New York"


@pytest.mark.django_db
def test_profile_form_invalid_data():
    user = User.objects.create_user(username="testuser", password="A!s2d3f4g5h6")
    profile = Profile.objects.get(user=user)
    form = ProfileForm(
        data={
            "name": "",
            "age": -1,
        },
        instance=profile,
    )

    assert not form.is_valid()
    assert "name" in form.errors
    assert "age" in form.errors
