from fastapi import FastAPI, Request
import Dbal
from model import *
from pydantic import BaseModel
from datetime import datetime, time, date

from fastapi.middleware.cors import CORSMiddleware

# from fastapi import Path


# creating an object for FastAPI() class in order to use its methods
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Manager_DataType(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class Books_DataType(BaseModel):
    title: str
    author: str
    publisher: str
    number_of_books: int


class Student_DataType(BaseModel):
    name: str
    age: int
    address: str
    phone: str


class User(BaseModel):
    email: str
    password: str


class issue_DataType(BaseModel):
    book_id: int
    student_id: int
    date: date
    time: time


class Return_DataType(BaseModel):
    id: int


@app.post("/Add_Manager")
def Add_Mng(obj: Manager_DataType):
    objMng = Manager(
        first_name=obj.first_name,
        last_name=obj.last_name,
        email=obj.email,
        password=obj.password,
    )
    Dbal.Add_Manager(objMng)
    return {"message": "Successfully added New Manager."}


@app.get("/")
def Get_Mng():
    lst = []
    rows = Dbal.Get_Manager()
    for row in rows:
        objmanager = Manager(
            id=row[0],
            first_name=row[1],
            last_name=row[2],
            email=row[3],
            password=row[4],
        )
        lst.append(objmanager)
    return {"managers": lst}


@app.post("/login")
def login(obj: User):
    result = Dbal.Manager_byEmail(obj)

    if result:
        return {"message": "Login successfully"}
    else:
        return {"message": "Invalid username or password"}


@app.post("/Add_Books")
def Add_books(obj: Books_DataType):
    objBooks = Books(
        title=obj.title,
        author=obj.author,
        publisher=obj.publisher,
        number_of_books=obj.number_of_books,
    )
    Dbal.Add_NewBook(objBooks)
    return {"message": "New Book added in the library"}


@app.get("/Get_Books")
def Get_Books():
    alst = []
    rows = Dbal.Get_AllBooks()
    for row in rows:
        objBooks = Books(
            id=row[0],
            title=row[1],
            author=row[2],
            publisher=row[3],
            number_of_books=row[4],
        )
        alst.append(objBooks)
    return alst


@app.post("/Add_Student")
def Add_Student(obj: Student_DataType):
    objStudent = Student(
        name=obj.name, address=obj.address, age=obj.age, phone=obj.phone
    )
    Dbal.Add_NewStudent(objStudent)
    return {"message": "New Student added"}


@app.get("/Get_Student")
def Get_Students():
    blst = []
    rows = Dbal.Get_AllStudents()
    for row in rows:
        objStudent = Student(
            id=row[0], name=row[1], address=row[2], age=row[3], phone=row[4]
        )
        blst.append(objStudent)
    return blst


@app.put("/update")
def UpdateManager(obj: Manager_DataType):
    obj = Manager(
        id=obj.id,
        first_name=obj.first_name,
        last_name=obj.last_name,
        email=obj.email,
        password=obj.password,
    )
    Dbal.Update_Manager(obj)
    return {"message": "Updated the selected record"}


@app.post("/issue")
def issueRecord(obj: issue_DataType):
    message = Dbal.issuance(obj)
    return message


@app.get("/Get_Issue")
def get_Issue():
    clst = []
    rows = Dbal.Get_Allissue()
    for row in rows:
        objIssue = Issue(
            id=row[0], book_id=row[1], student_id=row[2], date=row[3], time=row[4]
        )
        clst.append(objIssue)
    return clst


@app.get("/Return_Record")
def getReturnRecord():
    clst = []
    rows = Dbal.Get_AllRecords()
    for row in rows:
        objIssue = Issue(
            id=row[0], book_id=row[1], student_id=row[2], date=row[3], time=row[4]
        )
        clst.append(objIssue)
    return clst


@app.get("/Return_Record/{id}")
def addReturnRecord(id: int):

    issue = Dbal.IssueBy_id(id)
    rcrd = Dbal.AddRecord(issue)

    if rcrd == None:
        return {"error": "something went wrong"}

    Dbal.DeleteIssue(id)

    return {"message": "record saved"}
