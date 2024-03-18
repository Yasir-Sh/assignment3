from database_init.db_connect import *
from database_init.db_create import *
import os

#Performs the get command to retrieve all students 
def get_all_students(cur):
    #executing the query for all students
    cur.execute("SELECT * FROM students")

    #printing result to terminal
    for row in cur.fetchall():
        print(row)

#Performs the add command to add a new student to the relation
def add_student(cur, conn, first_name, last_name, email, enrollment_date):
    #try/except block to handle errors
    try:
        #exectuing the INSERT query with the desired params
        cur.execute("INSERT INTO students (\
                    first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (
                    first_name, last_name, email, enrollment_date))
    except:
        #If invalid, informing user with common problems
        print("\nUnable to add student. Common Issues: \nFirst name is empty\nLast name is empty\nEmail is empty\nEmail is NOT unique\nInvalid date format")

    #Commiting the change to the database if it occurs
    conn.commit()

#Performs the update email command to change an exisiting email in the relation
def update_student_email(cur, conn, student_id, email):
    #try/except block to handle errors
    try :
        #exectuing the INSERT query with the desired params
        cur.execute("UPDATE students SET email = (%s) WHERE student_id = (%s)", (email, student_id))
    except:
        #If invalid, informing user with common problems
        print("\nUnable to change student email. Common Issues: \nStudent id is not in database\nStudent id is empty\nEmail is empty\nEmail is NOT unique\nNew email is the same as old email")

    #Commiting the change to the database if it occurs
    conn.commit()

#Performs the delete command to remove a student from the relation based on student id
def delete_student(cur, conn, student_id):
    #try/except block to handle errors
    try:
        #exectuing the INSERT query with the desired params
        cur.execute("DELETE FROM students WHERE student_id = (%s)", (student_id,))
    except:
        #If invalid, informing user with common problems
        print("\nUnable to change student email. Common Issues: \nStudent id is not in database\nStudent id is empty")
    conn.commit()

#Prints the instructions of the application
def instructions():
    print("\nProgram Use Instructions:\n")
    print("Type 'get' to get all students in database")
    print("Type 'add' to add a student")
    print("Type 'update' to update student email")
    print("Type 'delete' to delete a student")
    print("Type 'help' for instructions")
    print("Type 'exit' to exit program\n")

# main script

setup_student_relation() #Creating the student relation in the initial state
conn, cur = connect_to_database() #Connecting to database
instructions() #Printing instructions for the main program
exit = True

#Run until user exits
while exit:
    #get use command
    cmd = input("\nType one of the commands shown above: ")

    if cmd == "help":
        instructions() # Print instructions if cmd is help

    elif cmd == "exit":
        exit = False # Set exit to false -> exits program

    elif cmd == "get":
        get_all_students(cur) # Retrieves all students  

    elif cmd == "add":
        first_name = input("Type the first name of the student: ") # getting input for first name
        last_name = input("Type the last name of the student: ") # getting input for last name
        email = input("Type email of the student (email must be unique): ") # getting input for email
        enrollment_date = input("Type the enrollment date of the student (use YYYY-MM-DD format): ") # getting enrollment data
        add_student(cur, conn, first_name, last_name, email, enrollment_date) # Adding the student to students relation

    elif cmd == "update":
         student_id = input("Type the student id of the student: ") # getting input for student id 
         email = input("Type new email of the student (email must be unique): ") # getting input for new email
         update_student_email(cur, conn, student_id, email) # Updating the student's email by student id

    elif cmd == "delete":
        student_id = input("Type the student id of the student: ") # getting the student id
        delete_student(cur, conn, student_id) # deleting the student from students relation using the student id

    elif cmd == "clear":
        clear = lambda: os.system('cls') # getting a clear function
        clear() # flushing the terminal 

    else:
        # informing user of invalid command and printing the instructions
        print(f"invalid command: {cmd}. See instructions") 
        instructions()

#closing database connection
close_connection(conn, cur)


