from fastapi.testclient import TestClient

from app.main import app
client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert "status" in response.json()


def test_get_students():
    response = client.get("/students")

    assert response.status_code == 200
    assert "items" in response.json()


def test_get_student_success():
    response = client.get("/students/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_student_not_found():
    response = client.get("/students/999999")

    assert response.status_code == 404


def test_create_student():
    data = {
        "name": "Test Student",
        "email": "test_student@gmail.com",
        "password": "123456",
        "phone": "0999999999",
        "age": 20,
        "is_active": True
    }

    response = client.post(
        "/students",
        json=data
    )

    assert response.status_code == 201

    student_id = response.json()["id"]

    client.delete(f"/students/{student_id}")


def test_create_duplicate_email():
    data = {
        "name": "Duplicate",
        "email": "an@gmail.com",
        "password": "123456",
        "phone": "0988888888",
        "age": 20,
        "is_active": True
    }

    response = client.post(
        "/students",
        json=data
    )

    assert response.status_code == 409


def test_create_invalid_data():
    data = {
        "name": "",
        "email": "invalid-email",
        "password": "123",
        "age": 200
    }

    response = client.post(
        "/students",
        json=data
    )

    assert response.status_code == 422


def test_put_student():
    data = {
        "name": "Updated Student",
        "email": "updated@gmail.com",
        "password": "123456",
        "phone": "0977777777",
        "age": 23,
        "is_active": True
    }

    response = client.put(
        "/students/1",
        json=data
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Updated Student"


def test_patch_student():
    response = client.patch(
        "/students/1",
        json={
            "name": "Patched Student"
        }
    )

    assert response.status_code == 200
    assert response.json()["name"] == "Patched Student"


def test_delete_student():
    data = {
        "name": "Delete Test",
        "email": "delete_test@gmail.com",
        "password": "123456",
        "phone": "0966666666",
        "age": 20,
        "is_active": True
    }

    create_response = client.post(
        "/students",
        json=data
    )

    assert create_response.status_code == 201

    student_id = create_response.json()["id"]

    response = client.delete(
        f"/students/{student_id}"
    )

    assert response.status_code == 200


def test_search_filter_pagination():
    response = client.get(
        "/students/search",
        params={
            "keyword": "Student",
            "min_age": 18,
            "max_age": 30,
            "is_active": True,
            "page": 1,
            "page_size": 5
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "items" in data
    assert "page" in data
    assert "page_size" in data
    assert "total" in data
    assert "total_pages" in data


def test_invalid_pagination():
    response = client.get(
        "/students/search",
        params={
            "page": 0,
            "page_size": 101
        }
    )
    assert response.status_code == 422
