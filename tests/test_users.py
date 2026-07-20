import pytest

from models.user import User
from models.user_create import UserCreate
from models.user_patch import UserPatch
from models.user_update import UserUpdate

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


@pytest.mark.parametrize(
    "user_id, name, username, email",
    [
        (1, "Adam", "adamix", "adamix@gmail.com"),
        (2, "Kuba", "kubix", "kubix@gmail.com"),
    ],
)
def test_update_user(users_api, user_id, name, username, email):

    updated_user = UserUpdate(
        name=name,
        username=username,
        email=email,
    )

    response = users_api.update_user(user_id, updated_user)
    assert response.status_code == 200

    updated_user_response = User.model_validate(response.json())

    assert updated_user_response.id == user_id
    assert updated_user_response.name == updated_user.name
    assert updated_user_response.username == updated_user.username
    assert updated_user_response.email == updated_user.email

def test_patch_user(users_api):
    user_id = 1

    patched_user = UserPatch(
        email="janix@gmail.com",
    )

    response = users_api.patch_user(user_id, patched_user)
    assert response.status_code == 200

    patched_user_response = User.model_validate(response.json())
    assert patched_user_response.email == patched_user.email
    