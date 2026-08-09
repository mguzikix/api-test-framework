import pytest

from api.post_api import PostApi
from config import BASE_URL, TIMEOUT
from api.users_api import UsersApi
from api_client.client import ApiClient


@pytest.fixture(scope="session")
def client():
    return ApiClient(
        base_url=BASE_URL,
        timeout=TIMEOUT,
    )

@pytest.fixture
def users_api(client):
    return UsersApi(client)

@pytest.fixture
def post():
    return ApiClient(
        base_url=BASE_URL,
        timeout=TIMEOUT,
    )

@pytest.fixture
def post_api(post):
    return PostApi(post)
