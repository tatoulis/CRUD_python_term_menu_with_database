import mysql.connector
import queries



config = {
    'host' : 'localhost',
    'user' : 'root',
    'passwd': '******',
}
conn = mysql.connector.connect(**config)
myCursor = conn.cursor()
myCursor.execute('use individualproject_part_β')



def student_menu():
    while True:
        print('Student menu')
        print('1.List of all students')
        print('2.add a new student')
        print('3.Exit')
        choice=int(input("Enter your choice:"))
        if choice==1:
            queries.all_students()
        elif choice==2:
            queries.add_student()
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")

def trainer_menu():
    while True:
        print('Trainer menu')
        print('1.List of all trainers')
        print('2.add a new trainer')
        print('3.Exit')
        choice=int(input("Enter your choice:"))
        if choice==1:
            queries.all_trainers()
        elif choice==2:
            queries.add_trainer()
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")


def course_menu():
    while True:
        print('Course menu')
        print('1.List of all courses')
        print('2.add a new course')
        print('3.Exit')
        choice=int(input("Enter your choice:"))
        if choice==1:
            queries.all_courses()
        elif choice==2:
            queries.add_course()
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")



def assignment_menu():
    while True:
        print('Assignment menu')
        print('1.List of all assignments')
        print('2.add a new assignment')
        print('3.Exit')
        choice=int(input("Enter your choice:"))
        if choice==1:
            queries.all_assignments()
        elif choice==2:
            queries.add_assignment()
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")

def student_per_course_menu():
    while True:
        print('Student per course menu')
        print('1.list of courses')
        print('2.Add a student into a course')
        print('3.Exit')
        choice=int(input("Enter your choice:"))
        if choice==1:
            queries.all_studens_per_course()
        elif choice==2:
            queries.add_student_per_course()
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")

def trainer_per_course_menu():
    while True:
        print('Trainer per course menu')
        print('1.list of courses')
        print('2.Add a trainer into a course')
        print('3.Exit')
        choice=int(input("Enter your choice:"))
        if choice==1:
            queries.all_trainers_per_course()
        elif choice==2:
            queries.add_trainer_per_course()
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")


def assignments_per_course_menu():
    while True:
        print('Assignment per course menu')
        print('1.list of courses')
        print('2.Add an assignment into a course')
        print('3.Exit')
        choice=int(input("Enter your choice:"))
        if choice==1:
            queries.all_assignment_per_course()
        elif choice==2:
            queries.add_assignment_per_course()
        elif choice==3:
            break
        else:
            print("Wrong Choice! Select between 1 and 3")


while True:
        print("Main menu")
        print("1.Course")
        print("2.Trainer")
        print("3.Student")    
        print("4.Assigment")
        print("5.Student per course")
        print("6.Trainer per course")
        print("7.Assignments per course")
        print("8.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            course_menu()    
        elif choice==2:
            trainer_menu()    
        elif choice==3:
            student_menu()
        elif choice==4:
            assignment_menu()
        elif choice==5:
            student_per_course_menu()
        elif choice==6:
            trainer_per_course_menu()
        elif choice==7:
            assignments_per_course_menu()
        elif choice==8:
            break
        else:
            print("Wrong Choice! Select between 1 and 8")
