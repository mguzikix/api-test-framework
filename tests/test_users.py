import pytest


@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_get_user(users_api, user_id):
    response = users_api.get_user(user_id)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user_id
    assert data["username"]
    assert data["name"]
    assert "@" in data["email"]