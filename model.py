from datetime import datetime, time

class Manager:
    def __init__(self,id = 0,first_name = 'test',  last_name = 'test', email='test@gmail',password='test'):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email =email
        self.password =password

class Books:
    def __init__(self,id = 0 ,title = 'test',  author = 'test', publisher='test',number_of_books =1):
        self.id = id
        self.title = title
        self.author = author
        self.publisher=publisher
        self.number_of_books = number_of_books    


class Student:
    def __init__(self,id = 0,name = 'test',  address = 'test', age=10, phone ='12345'):
        self.id = id
        self.name = name
        self.address = address
        self.age = age
        self. phone =  phone         

class Issue:
    def __init__(self,id = 0, book_id = 1, student_id = 1, date= 2000-21-12, time=time):
        self.id = id
        self.book_id = book_id
        self.student_id = student_id
        self.date = date
        self.time = time         

class Return_records:
    def __init__(self,id=0, book_id = 1, student_id = 1, date= 2000-21-12, time=time):
        self.id = id
        self. book_id = book_id 
        self. student_id = student_id
        self.date = date
        self.time = time 