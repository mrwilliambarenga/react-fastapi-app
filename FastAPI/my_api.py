from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel


app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    group: str


class StudentUpdate(BaseModel):
    name: str = None
    age: int = None
    group: str = None


students = {
    1: {
        "name": "john",
        "age": 17,
        "group": "year 12"
    }
}


@app.get("/")
def index():
    return {"name": "First Data"}


# Path Parameters   (e.g. /get-student/1)
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view.", gt=0, lt=3)):
    return students.get(student_id, "Student not found")


# Query Parameters  (e.g. /get-by-name/?name=john)
@app.get("/get-by-name/")
def get_student(*, name: str = None):
    for s_id in students:
        if students[s_id]["name"] == name:
            return students[s_id]
    return "Student not found"


# Post Method
@app.post("/create-student/{student_id}")
def create_student(*, student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}

    students[student_id] = student
    return students[student_id]


# Put Method
@app.put("/update-student/{student_id}")
def update_student(*, student_id: int, student_update: StudentUpdate):
    if student_id not in students:
        return {"Error": "Student doesn't exist"}
    updates = student_update.model_dump(exclude_unset=True)
    for k, v in updates.items():
        students[student_id][k] = v
    return students[student_id]