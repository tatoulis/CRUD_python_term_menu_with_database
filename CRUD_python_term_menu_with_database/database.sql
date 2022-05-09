CREATE DATABASE IF NOT EXISTS individualproject_part_β;

USE individualproject_part_β;

CREATE TABLE assignment (
  idassignment INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(45) NULL,
  description VARCHAR(500) NULL,
  SubDateTime DATE NULL,
  OralMark INT NULL,
  TotalMark INT NULL,
  PRIMARY KEY (idassignment));

CREATE TABLE students (
idstudents INT NOT NUll AUTO_INCREMENT,
FirstName VARCHAR(45) NULL,
LastName VARCHAR(45) NULL,
BirthDate DATE NULL,
TuitionFees VARCHAR(45),
PRIMARY KEY (idstudents));

CREATE TABLE course (
idcourse INT NOT NULL AUTO_INCREMENT,
Title VARCHAR(45) NULL,
Stream VARCHAR(45) NULL,
Type VARCHAR(45) NULL,
StartDate DATE NULL,
EndDate DATE NULL, 
PRIMARY KEY (idcourse));

CREATE TABLE Trainer (
idtrainer INT NOT NUll AUTO_INCREMENT,
FirstName VARCHAR(45) NULL,
LastName VARCHAR(45) NULL,
Subject VARCHAR(45) NULL,
PRIMARY KEY (idtrainer));

CREATE TABLE StudentPerCourse (
idstudents int null,
idcourse int null,
FOREIGN KEY (idstudents)
REFERENCES students(idstudents),
FOREIGN KEY (idcourse)
REFERENCES course(idcourse));

CREATE TABLE TrainerPerCourse (
idtrainer int null,
idcourse int null,
FOREIGN KEY (idtrainer)
REFERENCES trainer(idtrainer),
FOREIGN KEY (idcourse)
REFERENCES course(idcourse));

CREATE TABLE AssignmentPerCourse (
idassignment int null,
idcourse int null,
FOREIGN KEY (idassignment)
REFERENCES assignment(idassignment),
FOREIGN KEY (idcourse)
REFERENCES course(idcourse));


INSERT INTO students (FirstName,LastName,BirthDate,TuitionFees)
VALUES ('Betsy', 'Hensley', '1991/10/11','2000'),
		('Macaulay', 'Snide', '1985/05/03', '2000'),
        ('Marley', 'Weir', '1988/07/09', '2200'),
        ('Harris', 'Kouma', '1995/06/08', '2400'),
        ('Cem', 'Abbott', '1979/08/23', '1800'),
        ('Mahi', 'Briggs', '1993/06/05','2200'),
        ('Marlie', 'Coleman', '1992/09/12', '2200'),
        ('Marcie', 'Cairns', '1993/05/06', '2200'),
        ('Maisy', 'Padilla', '1985/10/02', '2200'),
        ('Jevon', 'Cobb', '1982/12/03', '2400');


INSERT INTO trainer (FirstName,LastName,Subject)
VALUES ('Zaydan', 'Krause', 'python'),
		('Matias', 'Peterson', 'c#'),
        ('Dorothy', 'Finney', 'python'),
        ('Beatrix', 'Palacios', 'Java'),
        ('Krisha', 'Flower', 'java');


INSERT INTO course (Title,Stream,Type,StartDate,EndDate)
VALUES ('CB9', 'java', 'full time', '2020/10/10', '2021/03/15'),
		('CB9', 'c#', 'full time', '2021/01/05', '2021/06/10'),
        ('CB9', 'python', 'part time', '2020/09/05', '2021/02/09'),
        ('CB9', 'python', 'full time', '2021/05/05', '2021/10/16'),
        ('CB9', 'c#', 'part time', '2021/02/10', '2021/07/16');
        

INSERT INTO assignment (title,description,SubDateTime,OralMark,TotalMark)
VALUES ('project_1', 'python', '2021/10/12', '40', '75'),
		('project_2', 'python', '2021/05/15', '60', '80'),
        ('project_3', 'java', '2021/06/12', '50', '85'),
        ('project_4', 'c#', '2021/03/15', '55', '90');

select * from assignment;
select * from course;
select * from students;
select * from trainer;
select * from studentpercourse;
select * from assignmentpercourse;
select * from trainerpercourse;
