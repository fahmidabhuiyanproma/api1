from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {}
next_id = 1


class Student(BaseModel):
    name: str
    gpa: float


@app.get("/students")
def get_students():
    return students


@app.post("/students", status_code=201)
def create_student(student: Student):
    global next_id

    students[next_id] = student.model_dump()

    result = {
        "id": next_id,
        "student": student
    }

    next_id += 1
    return result


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")

    del students[student_id]

    return {"message": "Student deleted"}
