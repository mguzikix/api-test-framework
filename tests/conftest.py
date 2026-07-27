import pytest

from config import BASE_URL, TIMEOUT
from api.users_api import UsersApi
from api_client.client import ApiClient


@pytest.fixture(scope="session")
def client():
    return ApiClient(BASE_URL, TIMEOUT)

@pytest.fixture
def users_api(client):
    return UsersApi(client)

