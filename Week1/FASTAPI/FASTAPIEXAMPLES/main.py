from fastapi import FastAPI,HTTPException #Is we are imprortng thr 
from pydantic import BaseModel

app = FastAPI() # creating the instance of the FastAPI class 

# Because app is require to Configure the Setting etc and also the many things 

# create the data validation and the shape of the API response
class student(BaseModel):
    name : str
    rating : int 
    course : str

# set the temporary storage we add that data into that 
students = [
  {
    "student_id" : 1,
    "name": "Garv",
    "rating": 5,
    "course": "FastAPI"
  },
  {
       "student_id" : 2,
    "name": "Rahul",
    "rating": 4,
    "course": "Python"
  },
  {
       "student_id" : 3,
    "name": "Aman",
    "rating": 5,
    "course": "Django"
  },
  {
       "student_id" : 4,
    "name": "Priya",
    "rating": 3,
    "course": "Machine Learning"
  },
  {
       "student_id" : 5,
    "name": "Simran",
    "rating": 4,
    "course": "Data Science"
  },
  {
       "student_id" : 6,
    "name": "Karan",
    "rating": 5,
    "course": "React"
  },
  {
       "student_id" : 7,
    "name": "Neha",
    "rating": 2,
    "course": "JavaScript"
  },
  {
       "student_id" : 8,
    "name": "Arjun",
    "rating": 4,
    "course": "Artificial Intelligence"
  }
]

student_id = 1

#create student
@app.post('/student')
def create_student(student : student):
    global student_id

    next_id = student_id
    students[student_id] = student
    student_id +=1

    return {
        "message" : "The student Fetch Successfully",
        "student" : student
    }

#read all the student

@app.get('/students')
def read_all_student():
    return {
        "students" : students
    }

# Read the single Student
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id]

@app.put("/students/{student_id}")
def update_student(student_id : int , student : student):
    if student_id not in students:
      raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    students[student_id] = student

    return {
        "message" : "The student updated Successfully",
        "student" : students[student_id]
    }

@app.delete("/students/{student_id}")
def delete_student(student_id : int ):
    if student_id not in students:
      raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    del students[student_id] 

    return {
        "message" : "The student Deleted Successfully",
    }
