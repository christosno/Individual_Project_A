import datetime

#  checks the date input from the user
def validated_date(string):
    print("")
    print(string)
    while True:
        try:

            while True:
                try:
                    year = int(input("give the year (in four digits e.g 1990) : ").strip())
                    break
                except :
                    print("Has be digits")

            while True:
                try:
                    month = int(input("give the month : ").strip())
                    break
                except:
                    print("Has be digits")

            while True:
                try:
                    day = int(input("give the day : ").strip())
                    break
                except:
                    print("Has be digits")


            return datetime.date(year,month,day)

        except ValueError:
            print("### Out of range!! ###")
            print("### Please try again ##")
            print("")




# checks if the delivery time of the assignment has passed
def validate_assignment(assignment):
    # use datetime lib for curent datetime
    date_time_now = datetime.date.today()
    expires = "Not EXP"

    assignment_deadline = assignment.get_deadline()
    # check if the year has passed
    if int(assignment_deadline.year) < date_time_now.year:
        expires = "EXP"
    elif int(assignment_deadline.year) == date_time_now.year:
        # check if the month has passed, only if years are equal
        if int(assignment_deadline.month) < date_time_now.month:
            expires = "EXP"
        elif int(assignment_deadline.month) == date_time_now.month:
            # check if the day has passed, only if months are equal
            if int(assignment_deadline.day) < date_time_now.day:
                expires = "EXP"
    return expires



# ask the user how to proceed
def continue_menu(string1, string2, string3, string4 = "Main Menu"):
    contin = input("\t1: Continue {}\n\t2: {}\n\t3: {}\n\t4: {}\n\t ->".format(string1, string2, string3, string4))
    while contin not in ["1", "2", "3", "4"]:
        contin = input("\t1: Continue {}\n\t2: {}\n\t3: {}\n\t4: {}\n\t ->".format(string1, string2, string3, string4))
    return contin


# ask the user to continue in the same menu
def continue_in_the_same_menu(string1,):
    contin = input("\t1: Continue {}\n\t2: Main Menu\n\t3: Exit\n\t ->".format(string1))
    while contin not in ["1", "2", "3"]:
        contin = input("\t1: Continue {}\n\t2: Main Menu\n\t3: Exit\n\t ->".format(string1))
    return contin



# prints the menu of existing courses and asks if he wants to add a new one, return the meny choice
def def_the_course(private_school, message = ""):
    print("Give the course {}".format(message))
    if len(private_school) == 0:
        print("______________________")
        print("There is no courses!!")
        print("______________________")
    x = 1
    d = {}
    string = ""
    # add in string all the existing courses and put in the dictionary each course
    for cour in private_school:
        string += str(x) + ": " + private_school[cour].get_code() + "\n"
        d[str(x)] = cour
        x += 1
    # add in string the Create course choice
    string += str(x) + ": " + "Create course" "\n\t->"
    d[str(x)] = "Create course"

    choice = input(string)
    while True:
        try:
            # if the choice is a kay in the d dictionary , put the value of choice in cour variable
            my_cour = d[choice]
            break
        except:
            print("Choose a num from above")
            choice = input(string)

    return my_cour


# check if a trainer exists in privet school, using the first and last name
def check_for_trainers(private_school, first_name, last_name):

    for course in private_school:
        for tr in private_school[course].get_trainers_list():
            if tr.get_first_name() == first_name and tr.get_last_name() == last_name:
                return tr

    return False

# check if a trainer exists in a course, using the first and last name
def check_for_trainers_in_the_course(course, trainer, private_school):

    for tr in private_school[course].get_trainers_list():
        if tr.get_first_name() == trainer.get_first_name() and tr.get_last_name() == trainer.get_last_name():
            return True

    return False

# check if a student exists in privet school, using the first name, last name and birtdate
def check_for_students(private_school, first_name, last_name, birthdate):

    for course in private_school:
        for st in private_school[course].get_students_list():
            if st.get_first_name() == first_name and st.get_last_name() == last_name and st.get_birthdate() == birthdate:
                return st

    return False


# check if a student exists in privet school, using the first name, last name and birtdate
def check_for_students_in_the_course(course, student, private_school):
    for st in private_school[course].get_students_list():
        if st.get_first_name() == student.get_first_name() and st.get_last_name() == student.get_last_name() and st.get_birthdate() == student.get_birthdate():
            return True

    return False


# check if assignemnt exists in school, using the title
def check_for_assignment_in_the_course(course, assignment, private_school):
    for assign in private_school[course].get_assignments_list():
        if assign.get_title() == assignment.get_title() and assign.get_submit_date == assignment.get_submit_date:
            return True

    return False
