#the-lunch-rescue


full_name = input("What is your first and last name? ")
student_id = input("What is your student ID number? ")

student_list = ""
student_id = ""
add_student = ""
student_list = []
Volunteer_dates = ["Monday: 6pm","Tuesday: 6pm","Wednesday: 6pm","Thursday: 6pm","Wednesday: 6pm"]
location = "Dublin High"

    
student_list.append((full_name, student_id))
print("This is your info. Make sure it is correct:" + "\nName:" + full_name + "\nStudent ID:" + student_id)

start = input("\nWelcome to te Lunch Rescue!\n What would you like to do? \n Type ""volunteer"" to volunteer to take these lunches to a nearby shelter. Type ""take a lunch"" to take a lunch home. (make sure you spell it right!)")


if start == "Take a Lunch" or "take a lunch":
    lunchcount = input("How many lunches would you like to take home? The maximum amount is 5 lunches.")

    if (int(lunchcount) > 0) and (int(lunchcount) <= 5):
        print("You have selected " + str(lunchcount) + " lunches")
        add_student()
        print("You have now saved " + str(lunchcount) + " lunches from being wasted. Thank you, and we hope to see you again soon!")
    else:
        print("Please enter a number between 1 and 5")
        lunchcount = input("How many lunches would you like to take home? The maximum amount is 5 lunches.")
        print("You have selected " + str(lunchcount) + " lunches")
        add_student()
        print("You have now saved " + str(lunchcount) + " lunches from being wasted. Thank you, and we hope to see you again soon!")

if start == "Volunteer" or "volunteer":
    print(Volunteer_dates)
    choose_time_date = input("Choose a day to volunteer.\n The times are fixed. \nenter \n M for monday \n TU for Tuesday \n W for Wednesday \n TH for Thursday \n F for Friday:")
    if choose_time_date == "M":
        print("Great! You are set to volunteer at" + location + "On Monday at 6 pm")
    if choose_time_date == "TU":
         print("Great! You are set to volunteer at" + location + "On Tuesday at 6 pm")
    if choose_time_date == "W":
         print("Great! You are set to volunteer at" + location + "On Wednesday at 6 pm")
    if choose_time_date == "TH":
         print("Great! You are set to volunteer at" + location + "On Thursday at 6 pm")
    if choose_time_date == "F":
         print("Great! You are set to volunteer at" + location + "On Friday at 6 pm")

    
