from course import Course


# CREATE COURSE
#######################################################################################################################################

# generates a unique course code as a key in private school dictionary, also creates a new  Course instance as value
def create_course(private_school):
    dic_course = {"1":"python", "2":"java", "3":"c#", "4":"javascript"}
    dic_type = {"1":"full time", "2":"part time"}
    print("")
    # chouses the course language
    course_language = input("Give course language:\n\t1: Python\n\t2: Java\n\t3: C#\n\t4: JavaScript\n\n\t ->")
    # validate the input
    while course_language not in ["1", "2", "3", "4"]:
        print("Sorry, i don't understand")
        course_language = input("Give course language:\n\t1: Python\n\t2: Java\n\t3: C#\n\t4: JavaScript\n\n\t ->")
    # chouses the course type
    course_type = input("Give the course type:\n\t1: Full Time\n\t2: Part Time\n\n\t ->")
    # validate the input
    while course_type not in ["1", "2"]:
        print("Sorry, i don't understand")
        course_type = input("Give the course type:\n\t1: Full Time\n\t2: Part Time\n\n\t ->")

    description = input("Give the description of the course:\n")

    # put in a variable the last four digits for the course code, using the course_discription function
    course_code_discription = course_discription(course_language, course_type)
    # determines the number of the new course in relation to the number of the most recent same course
    courseCode = course_code(private_school, course_code_discription)
    # add in private school dictionary as key the course_code also create a new Course instance for the dict value
    private_school[courseCode] = Course(courseCode, description, dic_course[course_language], dic_type[course_type])
    print("")
    print("## SUCCESSFUL REGISTRATION ##")
    print("")





# return the last four characters from the course code (e.g. "CB13FTPY")
def course_discription(course_language, course_type):

    if course_language == "1" or course_language == "python":
        if course_type == "1" or course_type == "full time":
            return ("FTPY")
        else:
            return ("PTPY")

    elif course_language == "2" or course_language == "java":
        if course_type == "1" or course_type == "full time":
            return ("FTJV")
        else:
            return ("PTJV")

    elif course_language == "3" or course_language == "c#":
        if course_type == "1" or course_type == "full time":
            return ("FTC#")

        else:
            return ("PTC#")
    else:
        if course_type == "1" or course_type == "full time":

            return ("FTJS")
        else:
            return ("PTJS")

# generates the final course code
def course_code(private_school, course_code_discription):
    num = 1
    for course in private_school:
        if private_school[course].get_code()[4:] == course_code_discription:
            while num <= int(private_school[course].get_code()[2:4]):
                num += 1
    if num < 10 :
        course_code = "CB" + "0" + str(num) + course_code_discription
    else:
        course_code = "CB" + str(num) + course_code_discription

    return course_code
