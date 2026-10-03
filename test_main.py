
from fastapi.testclient import TestClient
from main import app, students
import main

client = TestClient(app)


def reset():
    students.clear()
    main.next_id = 1


def test_create_student():
    reset()

    response = client.post(
        "/students",
        json={"name": "Alice", "gpa": 3.9}
    )

    assert response.status_code == 201
    assert response.json()["student"]["name"] == "Alice"


def test_get_students():
    reset()

    client.post(
        "/students",
        json={"name": "Bob", "gpa": 3.5}
    )

    response = client.get("/students")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_delete_student():
    reset()

    client.post(
        "/students",
        json={"name": "Carol", "gpa": 3.0}
    )

    response = client.delete("/students/1")

    assert response.status_code == 200
    assert len(students) == 0

