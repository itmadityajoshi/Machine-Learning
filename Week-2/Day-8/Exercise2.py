

def ticket_price(age, is_student):

    #check if age is a valid numeric value.
    
    if not isinstance(age, int) or age < 0:
        print( "Invalid age entered. Please enter a non-negative integer.")
    else:
        pass

        if 0<= age <=12:
            print("children Ticket Price is $10.")
        elif 13<= age <=17:
            print("Teenagers Ticket price is $15.")
        elif is_student:
            print("Your Ticket price is $18")
        else:
            print("Adult Ticket price is $20")
         
age = int(input("Enter your Age Please : "))
is_student = bool(input("Are you a Student?\nIf not press Enter.: "))
ticket_price(age,is_student)