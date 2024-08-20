CREATE TABLE Books (
    id INT IDENTITY(1,1) PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    publisher VARCHAR(255),
    number_of_books INT
);
CREATE TABLE Student (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(200),
    age INT,
    phone VARCHAR(15)
);


CREATE TABLE Issue (
    id INT IDENTITY(1,1) PRIMARY KEY,
    book_id INT FOREIGN KEY REFERENCES Books(id),
    student_id INT FOREIGN KEY REFERENCES Student(id),
    date DATE,
    time TIME,
);

CREATE TABLE Manager (
    id INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
);

create table Return_records(
id INT IDENTITY (1,1) PRIMARY KEY,
book_id INT FOREIGN KEY REFERENCES Books(id),
student_id INT FOREIGN KEY REFERENCES Student(id),
date DATE,
time TIME,
);

-- delete from Books where id = 4
-- insert into Issue values (3,3,GETDATE(),GETDATE())

select * from Student
select * from Books
select * from Issue
select * from Manager  
select * from Return_records