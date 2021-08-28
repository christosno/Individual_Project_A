import random
import datetime
from new_course import course_discription, course_code
from course import Course
from per_ass import Person, Student, Trainer, Assignment

# ans the user the number of inputs
def num_of_inputs(string):

    while True:
        try:
            num = input("Give the num of {} to add: ".format(string)).strip().lstrip("0")
            num = int(num)
            break
        except:
            print("Please give a num!")

    return num


# add courses 
def add_courses_for_dummy_data(num):

    for i in range(num):
        course_language = random.choice(language)
        course_type = random.choice(type)
        course_code_discription = course_discription(course_language, course_type)

        courseCode = course_code(private_school, course_code_discription)
        courses_li.append(courseCode)

        if course_type == "full time":
            description = "Full Time"
        else:
            description = "Part Time"

        course = Course(courseCode, course_language, description, course_type)
        private_school[courseCode] = course
        print("## SUCCESSFUL REGISTRATION ##")

# add students
def add_students_for_dymmy_data(num):

    for i in range(num):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        year = random.randint(1980, 2000)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        date_birth = datetime.date(year,month,day)
        student = Student(first_name, last_name, date_birth)
        student.set_tuitions_fees(random.randint(2000,2500))
        course = random.choice(courses_li)
        private_school[course].add_student(student)
        # add students in one or two courses
        for i in range(random.randint(0,1)):
            new_course = random.choice(courses_li)

            if new_course != course:
                private_school[new_course].add_student(student)
                student.set_tuitions_fees(random.randint(2000,2500))



# add trainers
def add_trainer_for_dymmy_data(num):

    for i in range(num):

        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        subject = random.choice(subjects)
        trainer = Trainer(first_name, last_name, subject)
        course = random.choice(courses_li)
        private_school[course].add_trainer(trainer)



# add assgnments
def add_assignments_for_dymmy_data(num):

    for i in range(num):

        title_discription = random.choice(titles_discriptions)

        title = title_discription[0]
        discription = title_discription[1]

        submit_year = random.randint(2019, 2020)
        submit_month = random.randint(1, 12)
        submit_day = random.randint(1, 28)

        submit_day = datetime.date(submit_year, submit_month, submit_day)

        deadline_year = random.randint(2019, 2022)
        deadline_month = random.randint(1, 12)
        deadline_day = random.randint(1, 28)

        deadline = datetime.date(deadline_year, deadline_month, deadline_day)

        mark_for_code = random.randint(1,100)
        mark_for_oral = 100 - mark_for_code

        assignment = Assignment(title, discription, submit_day, deadline, mark_for_code, mark_for_oral)

        course = random.choice(courses_li)
        private_school[course].add_assignment(assignment)



####################################################################
language = ["python", "java", "c#", "javascript"]
type = ["full time", "part time"]

first_names = ["James", "John", "Robert", "Michael", "William", "David", "Richard", "Joseph", "Thomas", "Charles",
                "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth", "Barbara", "Susan", "Jessica", "Sarah", "Karen"]

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

subjects = ["python", "java", "javascript", "database", "c#", "full stack", "functions"]

titles_discriptions = [("tic tac toc", "game"), ("aliens", "game"), ("privet school breef", "breef"), ("privet school part A", "Part A") ]


private_school = {}
courses_li = []


def dummy_data():



    num = num_of_inputs("courses")
    add_courses_for_dummy_data(num)

    num = num_of_inputs("students")
    add_students_for_dymmy_data(num)

    num = num_of_inputs("trainers")
    add_trainer_for_dymmy_data(num)

    num = num_of_inputs("assignments")
    add_assignments_for_dymmy_data(num)


    return private_school
