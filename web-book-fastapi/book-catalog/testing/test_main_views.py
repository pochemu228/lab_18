from fastapi.testclient import TestClient
from fastapi import status
from main import app
import pytest


client = TestClient(app)


def test_root_view():
    response = client.get("/")
    response_data = response.json()
    expected_message = "Hello World"
    assert response.status_code == status.HTTP_200_OK
    assert response_data["docs"] == "/docs"
    assert response_data["message"] == expected_message

def test_root_view_custom_name():
    name = "Anna"
    query = {"name": name}
    response = client.get("/", params=query)
    response_data = response.json()

    expected_message = f"Hello {name}"

    assert response.status_code == status.HTTP_200_OK
    assert response_data["docs"] == "/docs"
    assert response_data["message"] == expected_message


@pytest.mark.parametrize(
    "name",
    [
        "BGPU",
        "Bob",
        "",
        "!@##$%",
    ]
)
def test_root_view_parametrized_name(name: str):
    query = {"name": name}
    response = client.get("/", params=query)
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_data["message"] == f"Hello {name}"
    assert response_data["docs"] == "/docs"