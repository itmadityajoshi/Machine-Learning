# Creating a simple grading system where a student's score is entered, and the program determines the corresponding grade.

def grade(score, name):
    if 90<= score <= 100:
        print(f"{name}. your grade is A")
    elif(80<=score < 90):
        print(f"{name}. your grade is B.")
    elif(70<= score < 80):
        print(f"{name}. your grade is C.")
    elif(60 <= score <70):
        print(f"{name}. your grade is D.")
    else:
        print(f"{name}. your grade is F.")


name = input("enter the name : ")
score = int(input("enter the score : "))

print(grade(score,name))








