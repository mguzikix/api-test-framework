import requests

from api_client.client import ApiClient
from models.user_create import UserCreate
from models.user_patch import UserPatch
from models.user_update import UserUpdate

class UsersApi:
    def __init__(self, client:ApiClient):
        self.client = client

    def get_user(self, user_id:int) -> requests.Response:
        return self.client.get(f"users/{user_id}")

    def get_all_users(self) -> requests.Response:
        return self.client.get("users")

    def create_user(self, user: UserCreate) -> requests.Response:
        return self.client.post("users", json_data=user.model_dump())

    def update_user(self, user_id: int, user: UserUpdate) -> requests.Response:
        return self.client.put(f"users/{user_id}", json_data=user.model_dump())

    def patch_user(self, user_id: int, user: UserPatch) -> requests.Response:
        return self.client.patch(f"users/{user_id}", json_data=user.model_dump(exclude_unset=True))

    def delete_user(self, user_id: int) -> requests.Response:
        return self.client.delete(f"users/{user_id}")
