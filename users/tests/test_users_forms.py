import pytest
from django.contrib.auth.models import User
from users.forms import UserRegisterForm


@pytest.mark.django_db
def test_user_register_form_valid():
    form = UserRegisterForm(
        data={
            "username": "testuser",
            "email": "test@example.com",
            "password1": "Str0ngP@ssw0rd!",
            "password2": "Str0ngP@ssw0rd!",
        }
    )
    print(form.errors)
    assert form.is_valid()


@pytest.mark.django_db
def test_user_register_form_invalid_due_to_password_mismatch():
    form = UserRegisterForm(
        data={
            "username": "testuser",
            "email": "test@example.com",
            "password1": "password123",
            "password2": "password321",
        }
    )
    assert not form.is_valid()


@pytest.mark.django_db
def test_user_register_form_invalid_due_to_duplicate_user():
    User.objects.create_user(
        username="testuser", email="test@example.com", password="password123"
    )
    form = UserRegisterForm(
        data={
            "username": "testuser",
            "email": "test2@example.com",
            "password1": "password123",
            "password2": "password123",
        }
    )
    assert not form.is_valid()
