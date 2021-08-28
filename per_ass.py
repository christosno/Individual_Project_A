from general_func import validate_assignment, validated_date
from info_func import give_tuition_fees, validate_mark


class Person:
    """Model for a person. A parent class for Student and Trainer """
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def set_first_name(self):
        new_first_name = input("Give new First name: ").strip().capitalize()
        self._first_name = new_first_name

    def get_last_name(self):
        return self._last_name

    def set_last_name(self):
        new_last_name = input("Give new Last name: ").strip().capitalize()
        self._last_name = new_last_name





class Student(Person):
    """Model for privet school student"""
    _students_num = 0

    def __init__(self, first_name, last_name, birthdate,):

        super().__init__(first_name, last_name)

        self._birthdate = birthdate
        self._tuitions_fees = 0
        Student._students_num += 1
        # use the _students_num to produce a unique id for student
        self._student_id = "ST" + str(Student._students_num)

    def get_student_id(self):
        return self._student_id

    def get_tuitions_fees(self):
        return self._tuitions_fees

    def get_birthdate(self):
        return self._birthdate

    def set_tuitions_fees(self, new_tuition_fees = 0):
        if new_tuition_fees == 0:
            self._tuitions_fees += give_tuition_fees()
        else:
            self._tuitions_fees += new_tuition_fees

    def set_birthdate(self):
        new_birthdate = validated_date("Give new date of birth")
        self._birthdate = new_birthdate

    def print_student_name_id(self):
        print(self._student_id, self._first_name, self._last_name)

    def print_a_student_info(self):
        """Print infos for the student"""
        print("\tid:",self._student_id)
        print("\tFirst Name:", self._first_name)
        print("\tLast Name:", self._last_name)
        print("\tDate Of Birth:", self._birthdate)
        print("\t" + "#"*(19 + len(str(self._tuitions_fees))))
        print("\t" + "# Tuitions Fees:", self._tuitions_fees, "#")
        print("\t" + "#"*(19 + len(str(self._tuitions_fees))))
        print("")





class Trainer(Person):
    """Model for privet school trainer"""
    _trainers_num = 0

    def __init__(self, first_name, last_name, subject):

        super().__init__(first_name, last_name)

        self._subject = subject
        Trainer._trainers_num += 1
        # use the _trainers_num to produce a unique id for trainer
        self._trainer_id = "TR" + str(Trainer._trainers_num)

    def get_trainer_id(self):
        return self._trainer_id

    def get_subject(self):
        return self._subject

    def set_subject(self):
        new_subject = input("Give the new trainer's subject:").strip().capitalize()
        self._subject = new_subject

    def print_trainer_name_id(self):
        print(self._trainer_id, self._first_name, self._last_name)

    def print_a_trainer_info(self):
        """Print infos for the trainer"""
        print("\tid:",self._trainer_id)
        print("\tFirst Name:", self._first_name)
        print("\tLast Name:", self._last_name)
        print("\tSubject:", self._subject)
        print("")





class Assignment:
    """Model for privet school assignment"""
    _assignments_num = 0
    def __init__(self, title, description, submit_date, deadline, mark_for_code, mark_for_oral):
        self._title = title
        self._description = description
        self._submit_date = submit_date
        self._deadline = deadline
        self._mark_for_code = mark_for_code
        self._mark_for_oral = mark_for_oral
        Assignment._assignments_num += 1
        # use the _assignments_num to produce a unique id for assignment
        self._assignment_id ="AS" + str(Assignment._assignments_num)
        self._courses = []

    def get_title(self):
        return self._title

    def set_title(self):
        new_title = input("Give the new title: ")
        self._title = new_title

    def get_description(self):
        return self._description

    def get_submit_date(self):
        return self._submit_date

    def set_description(self):
        new_description =  input("Give the Discription: ").strip().capitalize()
        self._description = new_description

    def get_assignment_id(self):
        return self._assignment_id

    def get_mark_for_code(self):
        return self._mark_for_code

    def set_mark_for_code(self):

        mark_code_oral = validate_mark()

        new_mark_code = mark_code_oral[0]
        new_mark_oral = mark_code_oral[1]

        self._mark_for_code = new_mark_code
        self._mark_for_oral = new_mark_oral

    def get_deadline(self):
        return self._deadline

    def set_deadline(self):
        new_deadline = validated_date("Give new deadline")
        self._deadline = new_deadline

    def print_assignment_title_id(self):
        print(self._assignment_id, self._title)

    def print_an_assignment_info(self, exp_notexp):
        """Print infos for the assignment"""
        print("\tid:",self._assignment_id)
        print("\tTitle:", self._title)
        print("\tDescription:", self._description)
        print("\tSubmition Date:", self._submit_date)
        print("\tdeadline:", self._deadline, exp_notexp)
        print("\tMark for the Submitted Code:", self._mark_for_code)
        print("\tMark for the Oral Mark:", self._mark_for_oral)
        print("")

