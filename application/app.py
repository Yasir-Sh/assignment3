from database_init.db_connect import *
from database_init.db_create import *
import os

def get_all_students(cur):
    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        print(row)

def add_student(cur, conn, first_name, last_name, email, enrollment_date):
    try:
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    except:
        print("\nUnable to add student. Common Issues: \nFirst name is empty\nLast name is empty\nEmail is empty\nEmail is NOT unique\nInvalid date format")
    conn.commit()

def update_student_email(cur, conn, student_id, email):
    try :
        cur.execute("UPDATE students SET email = (%s) WHERE student_id = (%s)", (email, student_id))
    except:
        print("\nUnable to change student email. Common Issues: \nStudent id is not in database\nStudent id is empty\nEmail is empty\nEmail is NOT unique\nNew email is the same as old email")
    conn.commit()

def delete_student(cur, conn, student_id):
    try:
        cur.execute("DELETE FROM students WHERE student_id = (%s)", (student_id,))
    except:
        print("\nUnable to change student email. Common Issues: \nStudent id is not in database\nStudent id is empty")
    conn.commit()

def instructions():
    print("\nProgram Use Instructions:\n")
    print("Type 'get' to get all students in database")
    print("Type 'add' to add a student")
    print("Type 'update' to update student email")
    print("Type 'delete' to delete a student")
    print("Type 'help' for instructions")
    print("Type 'exit' to exit program\n")

# main script
setup_student_relation()
conn, cur = connect_to_database()
instructions()
exit = True

while exit:
    cmd = input("\nType one of the commands shown above: ")

    if cmd == "help":
        instructions()
    elif cmd == "exit":
        exit = False
    elif cmd == "get":
        get_all_students(cur,)
    elif cmd == "add":
        first_name = input("Type the first name of the student: ")
        last_name = input("Type the last name of the student: ")
        email = input("Type email of the student (email must be unique): ")
        enrollment_date = input("Type the enrollment date of the student (use YYYY-MM-DD format): ")
        add_student(cur, conn, first_name, last_name, email, enrollment_date)
    elif cmd == "update":
         student_id = input("Type the student id of the student: ")
         email = input("Type new email of the student (email must be unique): ")
         update_student_email(cur, conn, student_id, email)
    elif cmd == "delete":
        student_id = input("Type the student id of the student: ")
        delete_student(cur, conn, student_id)
    elif cmd == "clear":
        clear = lambda: os.system('cls')
        clear()
    else:
        print(f"invalid command: {cmd}. See instructions")
        instructions()



close_connection(conn, cur)


