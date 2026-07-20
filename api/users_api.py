from api_client.client import ApiClient
import requests
from models.user_create import UserCreate

class UsersApi:
    def __init__(self, client:ApiClient):
        self.client = client

    def get_user(self, user_id:int) -> requests.Response:
        return self.client.get(f"users/{user_id}")

    def get_all_users(self) -> requests.Response:
        return self.client.get("users")

    def create_user(self, user: UserCreate) -> requests.Response:
        return self.client.post("users", json_data=user.model_dump())