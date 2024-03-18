from database_init.db_connect import *
from database_init.db_create import *

def get_all_students(cur):
    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        print(row)
    print("\n")

def add_student(cur, conn, first_name, last_name, email, enrollment_date):
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    conn.commit()

def update_student_email(cur, conn, student_id, email):
    cur.execute("UPDATE students SET email = (%s) WHERE student_id = (%s)", (email, student_id))
    conn.commit()

def delete_student(cur, conn, student_id):
    cur.execute("DELETE FROM students WHERE student_id = (%s)", (student_id,))
    conn.commit()


# main script
setup_student_relation()
conn, cur = connect_to_database()

get_all_students(cur)

# add_student(cur, conn, 'Yasir', 'Sheikh', 'ysheikh1234@gmail.com', '2020-08-07')
# get_all_students(cur)

# update_student_email(cur, conn, 10, 'ysheikh213@gmail.com')
# get_all_students(cur)

# delete_student(cur, conn, 10)
# get_all_students(cur)

close_connection(conn, cur)


