from database_init.db_connect import *

def create_students_relation():
    conn, cur = connect_to_database()
    cur.execute("""CREATE TABLE IF NOT EXISTS students (
                student_id       SERIAL PRIMARY  KEY,
                first_name       VARCHAR(255)    NOT NULL,
                last_name        VARCHAR(255)    NOT NULL,
                email            VARCHAR(255)    UNIQUE NOT NULL,
                enrollment_date  DATE 
                )
                """)
    conn.commit()
    close_connection(conn, cur)

def clear_student_relations():
    conn, cur = connect_to_database()
    cur.execute("""DELETE FROM students""")
    cur.execute("""ALTER SEQUENCE students_student_id_seq RESTART WITH 1""")
    conn.commit()
    close_connection(conn, cur)

def populate_students_relation():
    conn, cur = connect_to_database()
    cur.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
                ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
                ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
                ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
                """)
    conn.commit()
    close_connection(conn, cur)



