import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_users_list(api):
    r = api.get(f"{BASE_URL}/users")
    assert r.status_code == 200
    assert len(r.json()) == 10          # тут ровно 10 пользователей


def test_get_single_user(api):
    r = api.get(f"{BASE_URL}/users/1")
    assert r.status_code == 200
    assert r.json()["id"] == 1


def test_create_post(api):
    payload = {"title": "foo", "body": "bar", "userId": 1}
    r = api.post(f"{BASE_URL}/posts", json=payload)
    assert r.status_code == 201          # 201 Created
    body = r.json()
    assert body["title"] == "foo"
    assert "id" in body


def test_user_not_found(api):
    r = api.get(f"{BASE_URL}/users/9999")  # такого нет
    assert r.status_code == 404            # негативный кейс


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_existing_users(api, user_id):
    r = api.get(f"{BASE_URL}/users/{user_id}")
    assert r.status_code == 200
    assert r.json()["id"] == user_id
