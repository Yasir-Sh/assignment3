from database_init.db_connect import *

#creates the students relation
def create_students_relation():
    #Setting up database connection
    conn, cur = connect_to_database()

    #executing the create query 
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
                student_id       SERIAL PRIMARY  KEY,
                first_name       VARCHAR(255)    NOT NULL,
                last_name        VARCHAR(255)    NOT NULL,
                email            VARCHAR(255)    UNIQUE NOT NULL,
                enrollment_date  DATE 
                )
                """)
    # Commiting the change to the database
    conn.commit()
    close_connection(conn, cur)

#Clears the student relations
def clear_student_relations():
    #Setting up database connection
    conn, cur = connect_to_database()

    #executing the query to delete all entries from database and reset the SERIAL student id
    cur.execute("""DELETE FROM students""")
    cur.execute("""ALTER SEQUENCE students_student_id_seq RESTART WITH 1""")

    # Commiting the change to the database
    conn.commit()
    close_connection(conn, cur)

#Populating the students relation with data
def populate_students_relation():
    #Setting up database connection
    conn, cur = connect_to_database()

    #executing the query to Insert students into the initial database
    cur.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
                ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
                ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
                ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
                """)
    
    # Commiting the change to the database
    conn.commit()
    close_connection(conn, cur)



