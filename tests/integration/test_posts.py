import pytest

from models.posts import Post, PostCreate, PostUpdate, PostPatch
from tests.integration.conftest import post_api


@pytest.mark.parametrize("post_id", [1, 5, 10])
def test_get_post(post_api, post_id):
    response = post_api.get_post(post_id)
    assert response.status_code == 200

    post = Post.model_validate(response.json())

    assert post.id == post_id
    assert post.userId
    assert post.title
    assert post.body

def test_get_all_posts(post_api):
    response = post_api.get_all_posts()

    assert response.status_code == 200

    posts = response.json()

    assert isinstance(posts, list)
    assert len(posts) > 0

@pytest.mark.parametrize(
    "title, body, user_id",
    [
        ("Test1", "Lorem ipsum dolor sit amet consectetur adipiscing elit. Quisque faucibus ex sapien vitae", 1),
        ("Test2", "Tempus leo eu aenean sed diam urna tempor. Pulvinar vivamus fringilla lacus nec metus", 2),
    ],
)
def test_create_post(post_api, title, body, user_id):
    new_post = PostCreate(
        title=title,
        body=body,
        userId = user_id
    )

    response = post_api.create_post(new_post)

    assert response.status_code == 201

    created_post = Post.model_validate(response.json())

    assert created_post.title == new_post.title
    assert created_post.body == new_post.body
    assert created_post.userId == user_id
    assert created_post.id > 0

def test_update_post(post_api):

    updated_post = PostUpdate(
        title="Test3",
        body="Lorem ipsum dolor sit amet consectetur adipiscing elit",
        UserId=2
    )

    post_id = 1

    response = post_api.update_post(post_id, updated_post)
    assert response.status_code == 200

    updated_post_response = PostUpdate.model_validate(response.json())

    assert updated_post_response.title == updated_post.title
    assert updated_post_response.body == updated_post.body


def test_patch_post(post_api):
    post_id=1

    patched_post = PostPatch(
        title="Test999",
    )

    response = post_api.patch_post(post_id, patched_post)
    assert response.status_code == 200

    patched_post_response = Post.model_validate(response.json())
    assert patched_post_response.title == patched_post.title


def test_delete_post(post_api):
    post_id = 1
    response = post_api.delete_post(post_id)

    assert response.status_code == 200