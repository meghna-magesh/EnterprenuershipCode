#the-lunch-rescue


full_name = input("What is your first and last name? ")
student_id = input("What is your student ID number? ")

student_list = "
add_student = ""
student_list = []
Volunteer_dates = ["Monday: 6pm","Tuesday: 6pm","Wednesday: 6pm","Thursday: 6pm","Wednesday: 6pm"]
location = "Dublin High"

    
student_list.append((full_name, student_id))
print("This is your info. Make sure it is correct:" + "\nName:" + full_name + "\nStudent ID:" + (str(student_id)))

while True:
  start = input("\nWelcome to the Lunch Rescue!\n What would you like to do? \n Type ""volunteer"" to volunteer to take these lunches to a nearby shelter. Type ""take a lunch"" to take a lunch home. (make sure you spell it right!)")
  
  if start.lower() == ("take a lunch") or ("Take a lunch"):
      lunchcount = int(input("How many lunches would you like to take home? The maximum amount is 5 lunches. "))
      if 0 < lunchcount <= 5:
          print("You have selected", lunchcount, "lunches.")
          print("You have now saved", lunchcount, "lunches from being wasted. Thank you, and we hope to see you again soon!")
          break
      else:
          print("Please enter a number between 1 and 5.")
  
  elif start.lower() == ("volunteer") or ("Volunteer"):
      print("Available Volunteer Dates:")
      for date in Volunteer_dates:
          print(date)
      choose_time_date = input("Choose a day to volunteer (M for Monday, TU for Tuesday, W for Wednesday, TH for Thursday, F for Friday): ").upper()
      if choose_time_date in ["M", "TU", "W", "TH", "F"]:
          print("Great! You are set to volunteer at", location, "on", choose_time_date, "at 6 pm.")
          break
      else:
          print("Invalid input. Please choose from the provided options.")
  
  else:
      print("Sorry, you might've spelled that wrong.")
