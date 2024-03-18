from database_init.db_oper import *

#Clears, the old relation, creates a fresh table and populates with starting values
def setup_student_relation():
    clear_student_relations()
    create_students_relation()
    populate_students_relation()