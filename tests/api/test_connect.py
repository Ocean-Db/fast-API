from faker import Faker
from fastapi.testclient import TestClient

from tests.conftest import api_client

fake = Faker()


class TestConnectDB:
    def test_post_data(self, api_client: TestClient):
        response = api_client.post(
            "/connect_db/",
            json={
                "username": fake.user_name(),
                "password": fake.password(),
                "db_name": fake.word(),
                "host": fake.ipv4(),
                "port": fake.port_number()
            }
        )
        pass
