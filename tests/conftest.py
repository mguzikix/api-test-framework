import pytest

from api.users_api import UsersApi
from api_client.client import ApiClient

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def client():
    return ApiClient(BASE_URL)

@pytest.fixture
def users_api(client):
    return UsersApi(client)

