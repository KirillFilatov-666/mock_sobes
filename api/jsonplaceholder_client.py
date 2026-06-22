"""Клиент для jsonplaceholder — методы по эндпоинтам, тесты не дёргают голый requests."""

from api.base_client import BaseClient


class JsonPlaceholderClient(BaseClient):
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self, session=None):
        super().__init__(self.BASE_URL, session)

    def get_users(self):
        return self.get("/users")

    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")

    def create_post(self, payload):
        return self.post("/posts", json=payload)
