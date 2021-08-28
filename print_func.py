from general_func import validate_assignment
# prints all students, checks not to print one student more than once
def print_all_students(private_school):
    print("")
    print("ALL THE STUDENTS")
    print("_________________")
    id_li = []
    i = 0
    for course in private_school:
        for student in private_school[course].get_students_list() :
            # check if the current id is in the id_li, if it is means that this student has already printed
            if student.get_student_id() in id_li:
                continue
            else:
                i += 1
                print(i, ".")
                student.print_a_student_info()

                id_li.append(student.get_student_id())

    if i == 0 :
        print("\tThere is no students")
        print("\t--------------------")


# prints all trainers, checks not to print one trainer more than once
def print_all_trainers(private_school):
    print("")
    print("ALL THE TRAINERS")
    print("_________________")
    id_li = []
    i = 0
    for course in private_school:
        for trainer in private_school[course].get_trainers_list():
            # check if the current id is in the id_li, if it is means that this trainer has already printed
            if trainer.get_trainer_id() in id_li:
                continue
            else:
                i += 1
                print(i, ".")
                trainer.print_a_trainer_info()

                id_li.append(trainer.get_trainer_id())

    if i == 0:
        print("\tThere is no trainers")
        print("\t--------------------")


# prints all assignments, checks not to print one assignment more than once
def print_all_assgnments(private_school):
    print("")
    print("ALL THE ASSIGNMENTS")
    print("___________________")
    id_li = []
    i = 0
    for course in private_school:
        for assignment in private_school[course].get_assignments_list():
            # check if the current id is in the id_li, if it is, means that this assignment has already printed
            if assignment.get_assignment_id() in id_li:
                continue
            else:
                i += 1
                # check if the deadline passed
                exp_notexp = validate_assignment(assignment)
                print(i, ".")
                assignment.print_an_assignment_info(exp_notexp)

                id_li.append(assignment.get_assignment_id())
    if i == 0:
        print("\tThere is no asiignments")
        print("\t-----------------------")


# print all the courses in private_school
def print_all_courses(private_school):
    print("")
    print("ALL THE COURSES")
    for i,course in enumerate(private_school):
        print(i + 1, ".")
        private_school[course].print_a_course()

# print all the students tha belong to more than one courses
def print_students_that_belong_to_more_than_one_courses(private_school):
    print("")
    print("STUDENTS THAT BELONG TO MORE THAN ONE COURSE")
    student_dict = {}
    i = 0
    # interation for each course
    for course in private_school:
        # interation for each student in course
        for student in private_school[course].get_students_list() :
            # check if the student is in student_dict
            if student not in student_dict:
                # if he isn't in student_dict, add the student as key and as value put one
                student_dict[student] = 1
            else:
                # if he is in the student_dict add one in value
                student_dict[student] += 1


    for k,v in student_dict.items():
        # check if the value is biger than 1, if it is print the student
        if v >= 2:
            i += 1
            print("\t",i, ")",k.get_student_id(), k.get_first_name(), k.get_last_name(), "in {} courses".format(v))

    if i == 0:
        print("\t--> There is no students that belong to more than one course <--")

    print("")
