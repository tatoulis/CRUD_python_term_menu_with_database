import mysql.connector

config = {
    'host' : 'localhost',
    'user' : 'root',
    'passwd': 'T@t43564356',
}
conn = mysql.connector.connect(**config)
myCursor = conn.cursor()
myCursor.execute('use individualproject_part_β')

def all_students():
    all_students_record = ('select * from students')
    myCursor.execute(all_students_record)
    print('-------------LIST FROM STUDENTS-------------')
    for(id,fn,ln,bd,tf)in myCursor:
        print(id,fn,ln,bd,tf)
        print('--------------------------------------------')

def all_trainers():
    all_trainers_record = ('select * from trainer')
    myCursor.execute(all_trainers_record)
    print('-------------LIST FROM TRAINERS-------------')
    for(id,fn,ln,sb)in myCursor:
        print(id,'|',fn,'|',ln,'|',sb)
        print('--------------------------------------------')

def all_assignments():
    all_assignments_record = ('select * from assignment')
    myCursor.execute(all_assignments_record)
    print('-------------LIST FROM ASSIGNMENTS-------------')
    for(id,ti,de,sd,om,tm)in myCursor:
        print(id,ti,de,sd,om,tm)
        print('--------------------------------------------')

def all_courses():
    all_courses_record = ('select * from course')
    myCursor.execute(all_courses_record)
    print('-------------LIST FROM COURSES-------------')
    for(id,ti,st,ty,sd,ed) in myCursor:
        print(id,ti,st,ty,sd,ed)
        print('--------------------------------------------')

def add_student():
    first_name = input('Give me the firts name:')
    last_name = input('Give me the last name:')
    birth_date = input('Give me the date of birthdate(yyyy/mm/dd):')
    tuition_fees = input('Give me the tuition fees:')
    add_student_record = ("insert into students (FirstName,LastName,BirthDate,TuitionFees)\
                           values ('{}', '{}', '{}', '{}')".format(first_name,last_name,birth_date,tuition_fees))
    myCursor.execute(add_student_record)
    print('------ SUCCESS ------\n')   

def add_trainer():
    first_name = input('Give me the firts name:')
    last_name = input('Give me the last name:')
    subject = input('Give me the subject:')
    add_trainer_record = ("insert into trainer (FirstName,LastName,subject)\
                           values ('{}', '{}', '{}')".format(first_name,last_name,subject))
    myCursor.execute(add_trainer_record)
    conn.commit()
    print('------ SUCCESS ------\n')

def add_assignment():
    title = input('Give me the title:')
    description = input('Give me a description:')
    SubDateTime = input('Give me the sub date (yyyy/mm/dd):')
    OralMark = int(input('Give me the oral mark:'))
    TotalMark = int(input('Give me the total mark:'))
    add_assignment_record = ("insert into assignment (title, description, SubDateTime,OralMark,TotalMark)\
                           values ('{}', '{}', '{}', '{}', '{}')".format(title, description, SubDateTime, OralMark, TotalMark))
    myCursor.execute(add_assignment_record)
    conn.commit()
    print('------ SUCCESS ------\n')

def add_course():
    Title = input('Give me the title:')
    Stream = input('Give me the stream:')
    Type = input('Give me the type:')
    StartDate = input('Give me the start date (yyyy/mm/dd):')
    EndDate = input('Give me the end date (yyyy/mm/dd):')
    add_course_record = ("insert into course (Title, Stream, Type, StartDate, EndDate)\
                        values ('{}', '{}', '{}', '{}', '{}')".format(Title, Stream, Type, StartDate, EndDate))
    myCursor.execute(add_course_record)
    conn.commit()
    print('------ SUCCESS ------\n')

def add_student_per_course():
    all_students = ('select idstudents, FirstName, LastName from students;')
    myCursor.execute(all_students)
    for(id,fn,ln)in myCursor:
        print(id,fn,ln)
        print('--------------------------------------------')
    student_id = int(input('select a student:'))
    all_courses = ('select idcourse,title,stream,type,startdate,enddate from course;')
    myCursor.execute(all_courses)
    for(id,ti,st,ty,sd,ed) in myCursor:
        print(id,ti,st,ty,sd,ed)
        print('--------------------------------------------')
    course_id = int(input('select a course:'))
    add_student_per_course_records = ("insert into studentpercourse(idstudents,idcourse)\
                                        values(%s,%s)")
    myCursor.execute(add_student_per_course_records, (student_id, course_id))
    conn.commit()

def all_studens_per_course():
    all_courses = ('select idcourse,title,stream,type,startdate,enddate from course;')
    myCursor.execute(all_courses)
    for(id,ti,st,ty,sd,ed) in myCursor:
        print(id,ti,st,ty,sd,ed)
        print('--------------------------------------------')
    course_id = int(input('select course id:'))
    all_studens_per_course_records = ("select students.FirstName, students.LastName\
                                     from studentpercourse\
                                     left join students\
                                     on studentpercourse.idstudents = students.idstudents\
                                     where studentpercourse.idcourse = {}".format(course_id))
    myCursor.execute(all_studens_per_course_records)
    print('-------LIST FROM STUDENT PER COURSE------------------')
    for(fn,ln) in myCursor:
        print(fn,ln)
        print('--------------------------------------------')


def add_trainer_per_course():
    all_trainers = ('select idtrainer, FirstName, LastName from trainer;')
    myCursor.execute(all_trainers)
    for(id,fn,ln)in myCursor:
        print(id,fn,ln)
        print('--------------------------------------------')
    trainer_id = int(input('select a trainer:'))
    all_courses = ('select idcourse,title,stream,type,startdate,enddate from course;')
    myCursor.execute(all_courses)
    for(id,ti,st,ty,sd,ed) in myCursor:
        print(id,ti,st,ty,sd,ed)
        print('--------------------------------------------')
    course_id = int(input('select a course:'))
    add_trainers_per_course_records = ("insert into trainerpercourse(idtrainer,idcourse)\
                                        values(%s,%s)")
    myCursor.execute(add_trainers_per_course_records, (trainer_id, course_id))
    conn.commit()

def all_trainers_per_course():
    all_courses = ('select idcourse,title,stream,type,startdate,enddate from course;')
    myCursor.execute(all_courses)
    for(id,ti,st,ty,sd,ed) in myCursor:
        print(id,ti,st,ty,sd,ed)
        print('--------------------------------------------')
    course_id = int(input('select course id:'))
    all_trainers_per_course_records = ("select trainer.FirstName, trainer.LastName\
                                     from trainerpercourse\
                                     left join trainer\
                                     on trainerpercourse.idtrainer = trainer.idtrainer\
                                     where trainerpercourse.idcourse = {}".format(course_id))
    myCursor.execute(all_trainers_per_course_records)
    print('-----------------LIST FROM TRAINERS PER COURSE-------------------')
    for(fn,ln) in myCursor:
        print(fn,ln)
        print('--------------------------------------------')


def add_assignment_per_course():
    all_assignments = ('select idassignment, title, description from assignment;')
    myCursor.execute(all_assignments)
    for(id,ti,de)in myCursor:
        print(id,ti,de)
        print('--------------------------------------------')
    assignment_id = int(input('select an assignment:'))
    all_courses = ('select idcourse,title,stream,type,startdate,enddate from course;')
    myCursor.execute(all_courses)
    for(id,ti,st,ty,sd,ed) in myCursor:
        print(id,ti,st,ty,sd,ed)
        print('--------------------------------------------')
    course_id = int(input('select a course:'))
    add_trainers_per_course_records = ("insert into assignmentpercourse(idassignment,idcourse)\
                                        values(%s,%s)")
    myCursor.execute(add_trainers_per_course_records, (assignment_id, course_id))
    conn.commit()

def all_assignment_per_course():
    all_courses = ('select idcourse,title,stream,type,startdate,enddate from course;')
    myCursor.execute(all_courses)
    for(id,ti,st,ty,sd,ed) in myCursor:
        print(id,ti,st,ty,sd,ed)
        print('--------------------------------------------')
    course_id = int(input('select course id:'))
    all_assignments_per_course_records = ("select assignment.title, assignment.description\
                                     from assignmentpercourse\
                                     left join assignment\
                                     on assignmentpercourse.idassignment = assignment.idassignment\
                                     where assignmentpercourse.idcourse = {}".format(course_id))
    myCursor.execute(all_assignments_per_course_records)
    print('--------------LIST FROM ASSIGNMENT PER COURSE-----------------')
    for(fn,ln) in myCursor:
        print(fn,ln)
        print('--------------------------------------------')

