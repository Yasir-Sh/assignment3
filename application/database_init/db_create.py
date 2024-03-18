from database_init.db_oper import *

def setup_student_relation():
    clear_student_relations()
    create_students_relation()
    populate_students_relation()