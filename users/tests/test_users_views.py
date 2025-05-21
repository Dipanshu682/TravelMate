import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from users.forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm


@pytest.mark.django_db
def test_register_view_get(client):
    url = reverse("register")
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context["form"], UserRegisterForm)


@pytest.mark.django_db
def test_register_view_post_valid(client):
    url = reverse("register")
    response = client.post(
        url,
        {
            "username": "testuser",
            "email": "test@example.com",
            "password1": "Str0ngP@ssw0rd!",
            "password2": "Str0ngP@ssw0rd!",
        },
    )
    if response.status_code != 302:
        print(response.context["form"].errors)
    assert (
        response.status_code == 302
    ), f"Unexpected status code: {response.status_code}"
    assert User.objects.filter(username="testuser").exists()


@pytest.mark.django_db
def test_register_view_post_invalid(client):
    url = reverse("register")
    response = client.post(
        url,
        {
            "username": "testuser",
            "email": "test@example.com",
            "password1": "password123",
            "password2": "password321",
        },
    )
    assert response.status_code == 200
    assert User.objects.count() == 0


@pytest.mark.django_db
def test_login_view_get(client):
    url = reverse("login")
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context["form"], AuthenticationForm)


@pytest.mark.django_db
def test_login_view_post_valid(client):
    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="password123"
    )
    url = reverse("login")
    response = client.post(
        url,
        {
            "username": "testuser",
            "password": "password123",
        },
    )
    assert response.status_code == 302
    assert response.wsgi_request.user.is_authenticated


@pytest.mark.django_db
def test_login_view_post_invalid(client):
    url = reverse("login")
    response = client.post(
        url,
        {
            "username": "testuser",
            "password": "wrongpassword",
        },
    )
    assert response.status_code == 200
    assert not response.wsgi_request.user.is_authenticated


@pytest.mark.django_db
def test_logout_view(client):
    user = User.objects.create_user(
        username="testuser", email="test@example.com", password="password123"
    )
    client.login(username="testuser", password="password123")
    url = reverse("logout")
    response = client.get(url)
    assert response.status_code == 302
    assert not response.wsgi_request.user.is_authenticated
