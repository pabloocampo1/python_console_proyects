
def to_continue(destination):
    question_continue=input(f"Do you want exit to {destination}? (yes/not)").lower()
    if question_continue == "yes":
        return True
    elif question_continue == "not":
        return False
    
def isValid_age():
    while True:
        try:
            age=int(input("age: "))
            if age >= 10 and age <= 100:
                return age
        except:
            print("data not valid")


