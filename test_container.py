import requests


def test_container_root():
    response = requests.get("http://localhost:8000/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Hello from Docker!"
    }


def test_container_add():
    response = requests.get(
        "http://localhost:8000/add",
        params={"a": 2, "b": 3}
    )

    assert response.status_code == 200
    assert response.json() == {
        "result": 5
    }