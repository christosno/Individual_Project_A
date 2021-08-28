from general_func import check_for_trainers_in_the_course, def_the_course,check_for_students_in_the_course, check_for_assignment_in_the_course
from info_func import give_tuition_fees

# ask the user if he want to keep or change the entry, and return he's choice
def keep_change(s, inst):
    print(s, ":", inst)
    choice = input("1: Keep the entry\n2: Change the entry\n -> ")
    while choice not in ["1", "2"]:
        print("Chouse between 1 and 2")
        choice = input("1: Keep the entry\n2: Change the entry\n -> ")
    return choice


# if the user user want to change the entry, this function call the suitable set fuction 
def edit(li_attributs, li_getFunc, li_setFunc):

    for i in range(len(li_attributs)):

        choice = keep_change(li_attributs[i], li_getFunc[i]())

        if choice == "2":

            li_setFunc[i]()



# print all the trainers and he's id,then asks the user for an id and try to find the trainer with this id
def find_a_trainer(private_school):

    for course in private_school:

        print("\t", course)

        private_school[course].print_trainers()

    choice_id = input("Give the trainer's id: ").strip().upper()


    for course in private_school:

        for tr in private_school[course].get_trainers_list():

            if tr.get_trainer_id() == choice_id:

                return tr

    return False



# print all the students and he's id,then asks the user for an id and try to find the student with this id
def find_a_student(private_school):

    for course in private_school:

        print("\t", course)

        private_school[course].print_students()

    choice_id = input("Give the student's id: ").strip().upper()


    for course in private_school:

        for st in private_school[course].get_students_list():

            if st.get_student_id() == choice_id:

                return st

    return False



# print all the assignments and it's id,then asks the user for an id and try to find the assignment with this id
def find_an_assignment(private_school):

    for course in private_school:

        print("\t", course)

        private_school[course].print_assignments()

    choice_id = input("Give the trainer's id: ").strip().upper()


    for course in private_school:

        for assign in private_school[course].get_assignments_list():

            if assign.get_assignment_id() == choice_id:
                return assign

    return False



# ask the user if he wants to add new course for the trainer, then add the trainer in the course if he doesn't exist in this course
def add_new_course_for_trainer(private_school, trainer, course):
    
    if not check_for_trainers_in_the_course(course, trainer, private_school):
        private_school[course].add_trainer(trainer)
    else:
        print("The trainer already exist in the {}".format(course))




# ask the user if he wants to add new course for the student, then add the student in the course if he doesn't exist in this course
def add_new_course_for_student(private_school, student, course):
    
    if not check_for_students_in_the_course(course, student, private_school):
        private_school[course].add_student(student)
        tuitios = give_tuition_fees()
        student.set_tuitions_fees(tuitios)
    else:
        print("The student already exist in the {}".format(course))



# ask the user if he wants to add new course for the assignment, then add the assignment in the course if it doesn't exist in this course
def add_new_course_for_assignment(private_school, assignment, course):

    if not check_for_assignment_in_the_course(course, assignment, private_school):
        private_school[course].add_assignment(assignment)
    else:
        print("The assignment already exist in the {}".format(course))

# remove the student fro mthe course if he is in the course
def remove_student_from_course(private_school, student, course):

    if check_for_students_in_the_course(course, student, private_school):
        private_school[course].remove_student(student)
        tuitios = give_tuition_fees()
        student.set_tuitions_fees(tuitios)
    else:
        print("The student doesn't exist in the {}".format(course))

# remove the trainer from the course if he is in the course
def remove_trainer_from_course(private_school, trainer, course):

    if  check_for_trainers_in_the_course(course, trainer, private_school):
        private_school[course].remove_trainer(trainer)
    else:
        print("The trainer doesn't exist in the {}".format(course))

# remove the assignment from the course if it is in the course
def remove_assignment_from_course(private_school, assignment, course):

    if  check_for_assignment_in_the_course(course, assignment, private_school):
        private_school[course].remove_assignment(assignment)
    else:
        print("The assignment doesn't exist in the {}".format(course))


# ask the user to add or remove course and return hew choice
def add_remove_course(string):
    print("Do you want to add or remove course for {}".format(string))
    add_remove_course = input("1: Add\n2: Remove\n3: Continue\n\t ->")
    while add_remove_course not in ["1", "2", "3"]:
        print("Please chouse a number from above")
        add_remove_course = input("1: Add\n2: Remove\n3: Continue\n\t ->")

    return add_remove_course   

