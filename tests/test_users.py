import pytest

from models.user import User
from models.user_create import UserCreate


INVALID_USER_ID = 999

@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_get_user(users_api, user_id):
    response = users_api.get_user(user_id)

    assert response.status_code == 200

    user = User.model_validate(response.json())

    assert user.id == user_id
    assert user.name
    assert user.username
    assert "@" in user.email

def test_get_non_existing_user_returns_404(users_api):
    response = users_api.get_user(INVALID_USER_ID)

    assert response.status_code == 404

@pytest.mark.parametrize(
    "name, username, email",
    [
        ("Adam", "adamix", "adamix@gmail.com"),
        ("Kuba", "kubix", "kubix@gmail.com"),
    ],
)
def test_create_user(users_api, name, username, email):
    new_user = UserCreate(
        name=name,
        username=username,
        email=email,
    )

    response = users_api.create_user(new_user)

    assert response.status_code == 201

    created_user = User.model_validate(response.json())

    assert created_user.name == new_user.name
    assert created_user.username == new_user.username
    assert created_user.email == new_user.email
    assert created_user.id > 0