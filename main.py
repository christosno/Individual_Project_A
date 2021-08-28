from course import Course
from per_ass import Person, Student, Trainer, Assignment
from menu import Main_Menu, Add_menu, Print_Menu, Edit_Menu
from new_course import course_discription, create_course, course_code
from info_func import *
from print_func import *
from general_func import *
from edit_func import *
from dummy_data import dummy_data

#MAIN PROGRAM
#####################################################################################

if __name__ == "__main__":

    print("\t#################################")
    print("\t# WELCOME TO THE PRIVET SCHOOL! #")
    print("\t#################################")
    print("")

    Main_Menu_Choice = None
    Add_Menu_Choice = None
    Print_choice = None
    contin = None

    # ask if the user want to use dummy data
    dummy_on_off = input("\t1: add data\n\t2: dummy data\n\t-> ")

    if dummy_on_off == "1":

        private_school = {}

    else:

        private_school = dummy_data()

    while Main_Menu_Choice != "4":
        # check if the user want to exit
        if Add_Menu_Choice == "5" or Print_choice == "11":
            break

        Main_Menu_Choice = Main_Menu()
        # user choice -> add course
        if Main_Menu_Choice == "0":

            while True:
                # create a Course instance and add in the private school
                create_course(private_school)
                # Ask the user if he want to continue creating new courses
                contin = continue_in_the_same_menu("to add courses")
                #enters the if statement only if he wants to stop creating courses
                if contin in ["2", "3"]:
                    break
            #enters the if statement only if he wants to exit
            if contin == "3":
                break

        # user choice -> add (student, trainer, assignment)
        elif Main_Menu_Choice == "1":

            while True:

                Add_Menu_Choice = Add_menu()

                # check if the user want to leave from add menu
                if Add_Menu_Choice == "4" or Add_Menu_Choice == "5":

                    break
                # user choice -> add trainer
                elif Add_Menu_Choice == "1":

                    while True:
                        # get infos for trainer from the user
                        trainer_info = Trainer_info()
                        # check if the trainer exists in privet school
                        trainer = check_for_trainers(private_school, trainer_info[0], trainer_info[1])
                        if not trainer:
                            # if doesn't exists create a new Trainer instance
                            trainer = Trainer(trainer_info[0], trainer_info[1], trainer_info[2])

                        else:
                            print("")
                            print("--> the trainer already exists <--")
                            print("")

                        while True:
                            # asks about the course that the trainer will enroll
                            course = def_the_course(private_school,"for trainer")
                            # if the course doesn't exist, create a new Course instance
                            while course == "Create course":
                                create_course(private_school)
                                course = def_the_course(private_school,"for trainer")
                            # check if the trainer exists in the course
                            if check_for_trainers_in_the_course(course, trainer, private_school):
                                print("")
                                print("--> the trainer already exist in the course <--")
                                print("")
                                same_trainer = "3"
                                break

                            # add the trainer in course's trainers_list
                            private_school[course].add_trainer(trainer)
                            # asks the user how he wants to continue( add new course for trainer, add new trainer, go to add menu , go to main menu)
                            same_trainer = continue_menu("add courses for the trainer","add new trainer", "add menu")
                            # check if the user want to leave from add courses for the trainer
                            if same_trainer in ["2", "3", "4"]:
                                break

                        # check if the user want to leave from add new trainer
                        if same_trainer in ["3", "4"]:
                            break

                    # check if the user want to leave from add menu
                    if same_trainer == "4":
                        break

                # user choice -> add student
                elif Add_Menu_Choice == "2":

                    while True:
                        # get infos for student from the user
                        student_info = Student_info()
                        # check if the student exists in privet school
                        student = check_for_students(private_school, student_info[0], student_info[1], student_info[2])

                        if not student:
                            # if doesn't exists create a new Student instance
                            student = Student(student_info[0], student_info[1], student_info[2])
                        else:
                            print("")
                            print("--> the student already exists <--")
                            print("")

                        while True:
                            # asks about the course that the student will enroll
                            course = def_the_course(private_school,"for student")
                            # if the course doesn't exist, create a new Course instance
                            while course == "Create course":
                                create_course(private_school)
                                course = def_the_course(private_school,"for student")
                            # check if the student exists in the course
                            if check_for_students_in_the_course(course, student, private_school):
                                print("")
                                print("--> the student already exist in the course <--")
                                print("")
                                same_student = "3"
                                break

                            # add the tuitions fees for this course to total student's tuitios fees
                            student.set_tuitions_fees()
                            # add the student in course's students_list
                            private_school[course].add_student(student)
                            # asks the user how he wants to continue( add new course for student, add new student, go to add menu , go to main menu)
                            same_student = continue_menu("add courses for the student", "add new student", "add menu")
                            # check if the user want to leave from add courses for the student
                            if same_student in ["2", "3", "4"]:
                                break

                        # check if the user want to leave from add new student
                        if same_student in ["3", "4"]:
                            break

                    # check if the user want to leave from add menu
                    if same_student == "4":
                        break

                # user choice -> add assignment
                elif Add_Menu_Choice == "3":

                    while True:
                        # get infos for assignment from the user
                        assignment_info = Assignment_info()
                        # create a new Assignment instance
                        assignment = Assignment(assignment_info[0], assignment_info[1], assignment_info[2], assignment_info[3], assignment_info[4], assignment_info[5])
                        while True:
                            # asks about the course that the assignment will enroll
                            course = def_the_course(private_school,"for assignemnt")
                            # if the course doesn't exist, create a new Course instance
                            while course == "Create course":
                                create_course(private_school)
                                course = def_the_course(private_school,"for assignemnt")
                            # check if the assignment exists in the course
                            if check_for_assignment_in_the_course(course, assignment, private_school):
                                print("")
                                print("--> the assignment already exist in the course <--")
                                print("")
                                same_assignment = "3"
                                break

                            # add the assignment in course's assignments_list
                            private_school[course].add_assignment(assignment)
                            # asks the user how he wants to continue( add new course for assignment, add new assignment, go to add menu , go to main menu)
                            same_assignment = continue_menu("add courses for the assignment", "add new assignment", "add menu")
                            # check if the user want to leave from add courses for the assignment
                            if same_assignment in ["2", "3", "4"]:
                                break
                        # check if the user want to leave from add new assignment
                        if same_assignment in ["3", "4"]:
                            break
                    # check if the user want to leave from add menu
                    if same_assignment == "4":
                        break

        # user choice -> Request Info
        elif Main_Menu_Choice == "2":

            while True:
                # ask the user about the request
                Print_choice = Print_Menu()

                # check if the user want to exit or go to main menu
                if Print_choice == "10" or Print_choice == "11" :
                    break
                # user choice -> Collection of all the students
                elif  Print_choice == "1":
                    # print all students
                    print_all_students(private_school)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> Collection of all the trainers
                elif Print_choice == "2":
                    # print all trainers
                    print_all_trainers(private_school)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> Collection of all the assignments
                elif Print_choice == "3":
                    # print all asignments
                    print_all_assgnments(private_school)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> Collection of all the courses
                elif Print_choice == "4":
                    # print all courses
                    print_all_courses(private_school)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> The students per course
                elif Print_choice == "5":
                    # iteretion for all the courses
                    for course in private_school:

                        print("\t#",private_school[course].get_code(),"#")
                        print("\t############")
                        # print all students for the course
                        private_school[course].print_students()
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> The trainers per course
                elif Print_choice == "6":
                    # iteretion for all the courses
                    for course in private_school:

                        print("\t#",private_school[course].get_code(),"#")
                        print("\t############")
                        # print all trainers for the course
                        private_school[course].print_trainers()
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> The assignments per course
                elif Print_choice == "7":
                    # iteretion for all the courses
                    for course in private_school:

                        print("\t#",private_school[course].get_code(),"#")
                        print("\t############")
                        # print all assignments for the course
                        private_school[course].print_assignments()
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> The assignments per student per course
                elif Print_choice == "8":
                    # iteretion for all the courses
                    for course in private_school:

                        print("\t#",private_school[course].get_code(),"#")
                        print("\t############")
                        # print all the assignments per student for all the students in the course
                        private_school[course].print_assignments_per_student()

                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> List of students that belong to more than one courses
                elif Print_choice == "9":

                    print_students_that_belong_to_more_than_one_courses(private_school)
                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the print menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break
            # check if the user want to leave from main menu
            if contin == "3":
                break

        # user choice -> Edit data
        if Main_Menu_Choice == "3":

            while True:
                # ask the user about the request
                edit_choice = Edit_Menu()
                # check if the user want to exit or go to main menu
                if edit_choice in ["4", "5"]:
                    break

                # user choice -> Edit trainer
                if edit_choice == "1":
                    # ask from user the trainer's id and check if trainer exist
                    trainer = find_a_trainer(private_school)

                    if not trainer:

                        print("\t--> There is no trainer <--")
                        print("")
                        break
                    # Lists we use in edit function
                    li_attributs = ["First Name", "Last Name", "Subject"]
                    li_getFunc = [trainer.get_first_name, trainer.get_last_name, trainer.get_subject]
                    li_setFunc = [trainer.set_first_name, trainer.set_last_name, trainer.set_subject]

                    # ask the user if he want to change or keep the entry
                    edit(li_attributs, li_getFunc, li_setFunc)
                    # ask the user if he want to add or remove course for the trainer
                    add_remove = add_remove_course("trainer")

                    if add_remove == "1":
                        course = def_the_course(private_school, "for the trainer")
                        add_new_course_for_trainer(private_school, trainer, course)
                    elif add_remove == "2":
                        course = def_the_course(private_school, "for the trainer")
                        remove_trainer_from_course(private_school, trainer, course)

                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the edit menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

                # user choice -> Edit student
                elif edit_choice == "2":
                    # ask from user the student's id and check if student exists
                    student = find_a_student(private_school)

                    if not student:

                        print("\t--> There is no student <--")
                        print("")
                        break

                    # Lists we use in edit function
                    li_attributs = ["First Name", "Last Name", "Date Of Birth"]
                    li_getFunc = [student.get_first_name, student.get_last_name, student.get_birthdate]
                    li_setFunc = [student.set_first_name, student.set_last_name, student.set_birthdate]
                    # ask the user if he want to change or keep the entry
                    edit(li_attributs, li_getFunc, li_setFunc)
                    # ask the user if he want to add or remove course for the student
                    add_remove = add_remove_course("student")

                    if add_remove == "1":
                        course = def_the_course(private_school, "for the student")
                        add_new_course_for_student(private_school, student, course)
                    elif add_remove == "2":
                        course = def_the_course(private_school, "for the student")
                        remove_student_from_course(private_school, student, course)

                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the edit menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break
                # user choice -> Edit assignment
                elif edit_choice == "3":
                    # ask from user the assignment's id and check if it exists
                    assignment = find_an_assignment(private_school)

                    if not assignment:

                        print("\t--> There is no assignment <--")
                        print("")
                        break

                    # Lists we use in edit function
                    li_attributs = ["Title", "Description", "Deadline", "Mark for the Submitted Code"]
                    li_getFunc = [assignment.get_title, assignment.get_description, assignment.get_deadline, assignment.get_mark_for_code]
                    li_setFunc = [assignment.set_title, assignment.set_description, assignment.set_deadline, assignment.set_mark_for_code]
                    # ask the user if he want to change or keep the entry
                    edit(li_attributs, li_getFunc, li_setFunc)
                    # ask the user if he want to add or remove course for the assignment
                    add_remove = add_remove_course("assignment")

                    if add_remove == "1":
                        course = def_the_course(private_school, "for the assignment")
                        add_new_course_for_assignment(private_school, assignment, course)
                    elif add_remove == "2":
                        course = def_the_course(private_school, "for the assignment")
                        remove_assignment_from_course(private_school, assignment, course)

                    # asks the user how he wants to continue(stay in the print menu or go to main menu or exit)
                    contin = continue_in_the_same_menu("in the edit menu")
                    # check if the user want to leave from print menu
                    if contin in ["2", "3"]:
                        break

            if contin == "3":
                break

            if edit_choice == "5":
                break

    print("")
    print("\t\tBYE BYE")
