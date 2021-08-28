from general_func import validate_assignment

class Course:
    """ Model of a course in Private school """
    def __init__(self, code, language, description, type):
        self._code = code
        self._language = language
        self._description = description
        self._type = type
        self._students_list = []
        self._trainers_list = []
        self._assignments_list = []

    def get_code(self):
        return self._code

    def get_language(self):
        return self._language

    def get_description(self):
        return self._description

    def get_type(self):
        return self._type

    def get_students_list(self):
        return self._students_list

    def get_trainers_list(self):
        return self._trainers_list

    def get_assignments_list(self):
        return self._assignments_list

    def add_student(self, student):
        """Add a student in course's students list """
        self._students_list.append(student)
        print("## SUCCESSFUL REGISTRATION ## / ID: {}".format(student.get_student_id()))
        print("")

    def remove_student(self, student):
        """Remove a student from course's students list"""
        self._students_list.remove(student)
        print("The student, {} {} removed from {}".format(student.get_first_name(), student.get_last_name(), self._code))
        print("")

    def remove_trainer(self, trainer):
        """Remove a trainer from course's trainers list"""
        self._trainers_list.remove(trainer)
        print("The trainer, {} {} removed from {}".format(trainer.get_first_name(), trainer.get_last_name(), self._code))
        print("")

    def remove_assignment(self, assignment):
        """Remove an assignment from course's assignments list"""
        self._assignments_list.remove(assignment)
        print("The asiignment, {} removed from {}".format(assignment.get_title(), self._code))
        print("")

    def add_trainer(self, trainer):
        """Add a trainer in course's trainer list """
        self._trainers_list.append(trainer)
        print("## SUCCESSFUL REGISTRATION ## / ID: {}".format(trainer.get_trainer_id()))
        print("")


    def add_assignment(self, assignment):
        """Add an assignment in course's assignments list """
        self._assignments_list.append(assignment)
        print("## SUCCESSFUL REGISTRATION ## / ID: {}".format(assignment.get_assignment_id()))
        print("")

    def print_a_course(self):
        """Print infos about the course"""
        print("\tCode:", self._code)
        print("\tLanguage:", self._language)
        print("\tDescription:", self._description)
        print("\tType:", self._type)
        print("\tNumber of students:", len(self._students_list))
        print("")
        print("")

    def print_students(self):
        """ Print infos for all students of the course using a method from Student class"""
        if len(self._students_list) == 0:
            print("\tNO STUDENTS IN THE COURSE")
        else:
            for i,student in enumerate(self._students_list):
                print("  ",i + 1, ")", end = " ")
                student.print_student_name_id()
        print("")



    def print_trainers(self):
        """ Print infos for all trainers of the course using a method from Trainer class"""
        if len(self._trainers_list) == 0:
            print("\tNO TRAINERS IN THE COURSE")
        else:
            for i,trainer in enumerate(self._trainers_list):
                print("  ",i + 1, ")", end = " ")
                trainer.print_trainer_name_id()
        print("")



    def print_assignments(self):
        """ Print infos for all the assignments of the course using a method from Assignment class"""
        if len(self._assignments_list) == 0:
            print("\tNO ASSIGNMENTS IN THE COURSE")
        else:
            for i,assignment in enumerate(self._assignments_list):
                print("  ",i + 1, ")", end = " ")
                assignment.print_assignment_title_id()
        print("")


    def print_assignments_per_student(self):
        """Print infos for assignments for each student who belong in the course"""
        if len(self._students_list) == 0:
            print("\tNO STUDENTS IN THE COURSE")
        else:
            for i,student in enumerate(self._students_list):
                print("  ",i + 1, ")",student._first_name,student._last_name)
                if len(self._assignments_list) == 0:
                    print("\tNO ASSIGNEMNTS FOR THE STUDENT")
                else:
                    for i,assignment in enumerate(self._assignments_list):
                        print("       ", i + 1, ")", assignment._title)
        print("")
