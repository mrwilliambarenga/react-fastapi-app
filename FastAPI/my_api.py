from typing import Optional
from fastapi import FastAPI, Path


app = FastAPI()


students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
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