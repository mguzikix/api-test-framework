import requests

from api_client.client import ApiClient
from models.posts import PostCreate, PostUpdate, PostPatch

class PostApi:
    def __init__(self, client:ApiClient):
        self.client = client

    def get_all_posts(self) -> requests.Response:
        return self.client.get("posts")

    def get_post(self, post_id:int) -> requests.Response:
        return self.client.get(f"posts/{post_id}")

    def create_post(self,post: PostCreate) -> requests.Response:
        return self.client.post(f"posts",json_data=post.model_dump())

    def update_post(self, post_id:int, post: PostUpdate) -> requests.Response:
        return self.client.put(f"posts/{post_id}",json_data=post.model_dump())

    def patch_post(self, post_id: int, post: PostPatch) -> requests.Response:
        return self.client.patch(f"posts/{post_id}",json_data=post.model_dump(exclude_unset=True))

    def delete_post(self, post_id: int) -> requests.Response:
        return self.client.delete(f"posts/{post_id}")
