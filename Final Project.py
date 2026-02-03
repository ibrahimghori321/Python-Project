from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# ----------- DATA STORE -----------
students = {}

# ----------- MODELS -----------
class Student(BaseModel):
    roll: str
    name: str

class Marks(BaseModel):
    roll: str
    marks: list[int]


# ----------- FUNCTIONS -----------
def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"


# ----------- API ROUTES -----------

@app.get("/")
def home():
    return {"message": "Student Grade Management API Running!"}


# 1. Add Student
@app.post("/add-student")
def add_student(data: Student):
    students[data.roll] = {
        "name": data.name,
        "marks": [],
        "grade": ""
    }
    return {"message": "Student added successfully!", "student": students[data.roll]}


# 2. Add Marks
@app.post("/add-marks")
def add_marks(data: Marks):
    if data.roll not in students:
        return {"error": "Student not found!"}

    students[data.roll]["marks"] = data.marks
    students[data.roll]["grade"] = calculate_grade(data.marks)

    return {"message": "Marks added successfully!", "student": students[data.roll]}


# 3. Display a Student
@app.get("/student/{roll}")
def display_student(roll: str):
    if roll not in students:
        return {"error": "Student not found!"}
    return students[roll]


# 4. Display All Students
@app.get("/all-students")
def all_students():
    return students