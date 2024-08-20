import pyodbc as p
from model import *
import time


def GetConnection():
    conn = p.connect(r"Driver=SQL Server;Server=SAMEERAMANSOORI;Database=LMS")
    return conn


def Get_Manager():
    conn = GetConnection() 
    cursor = conn.cursor()
    cursor.execute("select * from Manager")
    rows = cursor.fetchall()
    return rows


def Add_Manager(objMng):
    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute(
        f"Insert into Manager values('{objMng.first_name}','{objMng.last_name}', '{objMng.email}', '{objMng.password}')"
    )
    cursor.commit()
    print("New Employee Added Succesfully")
  


def Manager_byEmail(obj):
    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute(
        f"select email,password from Manager where email ='{obj.email}' and password ='{obj.password}'"
    )
    row = cursor.fetchone()

    print("\n\n", row, "\n\n")
    return row


def Get_AllBooks():
    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute("select * from Books")
    rows = cursor.fetchall()
    return rows


def Add_NewBook(objBooks):
    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute(
        f"Insert into Books values('{objBooks.title}','{objBooks.author}', '{objBooks.publisher}', {objBooks.number_of_books})"
    )

    print(
        "\n\n",
        f"Insert into Books values('{objBooks.title}','{objBooks.author}', '{objBooks.publisher}', {objBooks.number_of_books})",
        "\n\n",
    )

    cursor.commit()
    # print("New Book Added in the library")
    # Get_AllBooks()


def Get_AllStudents():
    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute("select * from Student")
    rows = cursor.fetchall()
    return rows


def Add_NewStudent(objStudent):
    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute(
        f"Insert into Student values('{objStudent.name}','{objStudent.address}', {objStudent.age}, '{objStudent.phone}')"
    )
    cursor.commit()
    print("New Student added")
    Get_AllStudents()


def Update_Manager(obj):
    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute(
        f"Update  Manager set first_name = '{obj.first_name}',last_name= '{obj.last_name}',email= '{obj.email}',password='{obj.password}' where id ={obj.id} "
    )
    cursor.commit()
    print(" Manager Updated Succesfully")
    Get_Manager()


def issuance(obj):
    conn = GetConnection()
    cursor = conn.cursor()
    print("\n\n", obj.time, "\n\n")
    print("\n\n", type(obj.time), "\n\n")
    _time = obj.time.strftime("%H:%M:%S")
    print(
        f"insert into Issue values({obj.book_id},{obj.student_id},'{obj.date}','{_time}')"
    )
    try:
        cursor.execute(
            f"insert into Issue values({obj.book_id},{obj.student_id},'{obj.date}','{_time}')"
        )
        cursor.commit()
        return {"message": "Book Issued"}
    except:
        return {"error": "Something went wrong"}


def Get_Allissue():
    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute("select * from Issue")
    rows = cursor.fetchall()
    return rows


def IssueBy_id(id):
    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute(f"select * from Issue where id = {id}")
    # cursor.execute(f"INSERT INTO Return_records (book_id,student_id ,date,time) SELECT book_id,student_id ,date,time FROM Issue WHERE id ={obj.id}")
    row = cursor.fetchone()
    # row = cursor.commit()
    return row


def DeleteIssue(id):
    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute(f"delete from Issue where id = {id}")
    cursor.commit()
    return "Deleted Succesfully"


def AddRecord(objRecord):
    conn = GetConnection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            f"Insert into Return_records values({objRecord.id},{objRecord.book_id},{objRecord.student_id}, '{objRecord.date}', '{objRecord.time}')"
        )
        cursor.commit()
        return "Record Added Succesfully"
    except Exception as e:
        return None


def Get_AllRecords():
    conn = GetConnection()
    cursor = conn.cursor()
    cursor.execute("select * from Return_records")
    rows = cursor.fetchall()
    return rows
