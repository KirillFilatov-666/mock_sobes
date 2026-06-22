import pytest
from faker import Faker

fake = Faker()


@pytest.mark.api
@pytest.mark.smoke
def test_get_users_list(jp_client):
    r = jp_client.get_users()
    assert r.status_code == 200
    assert len(r.json()) == 10


@pytest.mark.api
def test_get_single_user(jp_client):
    r = jp_client.get_user(1)
    assert r.status_code == 200
    assert r.json()["id"] == 1


@pytest.mark.api
def test_create_post(jp_client):
    # данные генерируем через Faker — каждый прогон уникальные
    payload = {
        "title": fake.sentence(),
        "body": fake.text(),
        "userId": fake.random_int(min=1, max=10),
    }
    r = jp_client.create_post(payload)
    assert r.status_code == 201
    body = r.json()
    assert body["title"] == payload["title"]
    assert "id" in body


@pytest.mark.api
def test_user_not_found(jp_client):
    r = jp_client.get_user(9999)
    assert r.status_code == 404


@pytest.mark.api
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_existing_users(jp_client, user_id):
    r = jp_client.get_user(user_id)
    assert r.status_code == 200
    assert r.json()["id"] == user_id
