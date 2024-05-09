#the-lunch-rescue

start = input("Welcome to te Lunch Rescue!\n What would you like to do? \n Type ""volunteer"" to volunteer to take these lunches to a nearby shelter. Type ""take a lunch"" to take a lunch home.")
student_list = []

def add_student():
    full_name = input("What is your first and last name? ")
    student_id = input("What is your student ID number? ")
    
    student_list.append((full_name, student_id))

if start == "Take a Lunch" or "take a lunch":
    lunchcount = input("How many lunches would you like to take home? The maximum amount is 5 lunches.")

    if (int(lunchcount) > 0) and (int(lunchcount) <= 5):
        print("You have selected " + str(lunchcount) + " lunches")
        add_student()
        print("You have now saved " + str(lunchcount) + " lunches from being wasted. Thank you, and we hope to see you again soon!")
    else:
        print("Please enter a number between 1 and 5")
        lunchcount = input("How many lunches would you like to take home? The maximum amount is 5 lunches.")


  



            
