# prints the main menu and returns our selection
def Main_Menu():
    print("\t\t~ MAIN MENU ~")
    print("")
    choice = input("\t0: Add course\n\t1: Add (student,trainer,assignment)\n\t2: Request Info\n\t3: Edit Data (student,trainer,assignmnt)\n\t4: Exit\n\t ->")
    while choice not in ["0","1","2","3","4"]:
        print("Sorry, i don't understand")
        print("Please chose again:")
        choice = input("\t0: Add course\n\t1: Add (student,trainer,assignment)\n\t2: Get Info\n\t3: Edit Data (student,trainer,assignmnt)\n\t4: Exit\n\t ->")

    return choice


# prints the add menu and returns our selection
def Add_menu():
    print("\t\t~ADD MENU~")
    print("")
    print("What do you want to add ")
    choice = input("\t1: trainer\n\t2: student\n\t3: assignment\n\t4: Main menu\n\t5: Exit\n\t ->")
    while choice not in ["1", "2", "3", "4", "5"]:
        print("Sorry, i don't understand")
        print("Please chose again:")
        choice = input("\t1: trainer\n\t2: student\n\t3: assignment\n\t4: Main menu\n\t5: Exit\n\t ->")

    return choice


# prints the print menu and returns our selection
def Print_Menu():
    print("\t\t~PRINT MENU~")
    print("")
    print("What do you want to print?")
    choice = input("\t1: Collection of all the students\n\t2: Collection of all the trainers\n\t3: Collection of all the assignments\n\t4: Collection of all the courses\n\t5: The students per course\n\t6: The trainers per course\n\t7: The assignments per course\n\t8: The assignments per student per course\n\t9: List of students that belong to more than one courses\n\t10: Main manu\n\t11: Exit\n\t ->")
    while choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
        print("Sorry, i don't understand")
        print("Please chose again:")
        choice = input("\t1: Collection of all the students\n\t2: Collection of all the trainers\n\t3: Collection of all the assignments\n\t4: Collection of all the courses\n\t5: The students per course\n\t6: The trainers per course\n\t7: The assignments per course\n\t8: The assignments per student per course\n\t9: List of students that belong to more than one courses\n\t10: Main manu\n\t11: Exit\n\t ->")

    return choice


# prints the edit menu and returns our selection
def Edit_Menu():
    print("\t\t~EDIT MENU~")
    print("")
    print("What do you want to edit ")
    choice = input("\t1: trainer\n\t2: student\n\t3: assignment\n\t4: Main menu\n\t5: Exit\n\t ->")
    while choice not in ["1", "2", "3", "4", "5"]:
        print("Sorry, i don't understand")
        print("Please chose again:")
        choice = input("\t1: trainer\n\t2: student\n\t3: assignment\n\t4: Main menu\n\t5: Exit\n\t ->")

    return choice
