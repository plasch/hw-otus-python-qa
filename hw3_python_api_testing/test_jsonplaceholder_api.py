import requests
import pytest

"""
Tests for REST API - https://jsonplaceholder.typicode.com/
{JSON} Placeholder - free fake API for testing and prototyping.
"""


@pytest.mark.parametrize("post_id", [4, 6, 89])
def test_get_resource(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == post_id, "Post's id doesn't match"


def test_creating_resource():
    headers = {"Content-type": "application/json; charset=UTF-8"}
    json = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", headers=headers, json=json)
    data = response.json()
    for i in json.keys():
        assert json[i] == data[i], "Resource was created incorrectly."


@pytest.mark.parametrize("filter_by, user_id", [
    ("posts", 1),
    ("todos", 5),
    ("albums", 3)
])
def test_filtering_resources(filter_by, user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/{filter_by}?userId={user_id}")
    data = response.json()
    for i in data:
        assert i["userId"] == user_id, "User's id doesn't match"


def test_get_albums_photo():
    albumId = 1
    response = requests.get(f"https://jsonplaceholder.typicode.com/albums/{albumId}/photos/")
    data = response.json()
    field = ["title", "url", "thumbnailUrl"]
    for i in data:
        assert i["albumId"] == albumId, "Album's id doesn't match"
    for i in field:
        assert i in data[0].keys(), "All fields are filled"
