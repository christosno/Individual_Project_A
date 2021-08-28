import datetime
from general_func import validated_date

#asks for the necessary inputs for a trainer and returns a tuple with that inputs
def Trainer_info():
    first_name = input("Give the Trainer's first name: ").strip().capitalize()
    last_name = input("Give the trainer's Last name: ").strip().capitalize()
    trainers_subject = input("Give the trainer's subject:").strip().capitalize()

    return (first_name, last_name, trainers_subject)



#asks for the necessary inputs for a student and returns a tuple with that inputs
def Student_info():
    first_name = input("Give student's first name: ").strip().capitalize()
    last_name = input("Give student's Last name: ").strip().capitalize()
    date_of_birth = validated_date("Give the day birth: ")

    return (first_name, last_name, date_of_birth)



# ask for the tuitions fees, validate the input and return it
def give_tuition_fees():
    while True:
        try:
            tuition_fees = int(input("Increase or Reduce(-) Tuition fees: ").strip())
            break
        except:
            print("Fees must be digits!!")

    return tuition_fees

# validate the mark_code , it must be up to 100, returns mark_coda and mark_oral
def validate_mark():
    mark_code = input("Mark for the submitted code: ")
    while (not mark_code.isdigit()) or int(mark_code) > 100 or int(mark_code) < 0:
        print("The input must be digit and between 0 and 100 ")
        mark_code = input("Mark for the submitted code: ")
    # calculates the mark_oral
    mark_oral = str(100 - int(mark_code))
    return (mark_code, mark_oral)


#asks for the necessary inputs for a assignment and returns a tuple with that inputs
def Assignment_info():
    datetime_now = datetime.datetime.now()
    title = input("Give the title: ").strip().capitalize()
    discription = input("Give the Discription: ").strip().capitalize()
    #get the current date
    date_of_submision = datetime.date.today()
    deadline = validated_date("Give the deadline: ")

    mark_code_oral = validate_mark()
    
    mark_code = mark_code_oral[0]
    mark_oral = mark_code_oral[1]

    return (title, discription, date_of_submision, deadline, mark_code, mark_oral)
