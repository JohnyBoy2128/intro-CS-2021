#   Program to take in an event from the user, along with appropriate dates and print them all out at the end
#   Assignment 8: Personal Organizer
#   John Paul Cannon
#   11 - 08 - 21


# function to check if a year is a leap year or not
def leapYear(y):
   if (y % 4 == 0 and y % 100 != 0):
      return 1
   elif (y % 400 == 0):
      return 1
   else:
      return 0


# Check for and adjust month input if necessary
def validateMonth(month):
   if (month < 1 or month > 12):
      return 1
   else:
      return month


# Check for and adjust day input if necessary
# (don't forget about leap year)
def validateDay(month, day, year):
   
   # array that holds the maximum amount of days in each month
   # 1st 0 in array is placeholder, so that january (1) will be index 1 and element 31
   maxDays = [0, 31, 28 + leapYear(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

   # this will check if the day entered is in the range of the possible amount of days in a month
   if (day > 0 and day <= maxDays[month]):
      return day
   else:
      return 1



# This function is used to print all events to the user in the format
# Event
# Date: Month Day, Year
def printEvents():
   
   # array to change month numbers to names
   # "" is a placeholder 
   monthNames = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
   
   print("")
   print("******************** List of Events ********************")

   # main loop to print all the arrays elements
   for i in range(len(eventName)):
      print(eventName[i])
      print("Date: " + monthNames[eventMonth[i]] + " " + str(eventDay[i]) + ", " + str(eventYear[i]))





# This function is used to prompt, adjust and
# append values to the 4 parallel arrays
def addEvent():
   
   # asking for user input for the event details
   name = input("What is the event: ")
   month = int(input("What is the month (number): "))
   day = int(input("What is the date: "))
   year = int(input("What is the year: "))

   # these will correct the day and the month, if needed
   month = validateMonth(month)
   day = validateDay(month, day, year)

   # appending all the values to their respective arrays
   eventName.append(name)
   eventMonth.append(month)
   eventDay.append(day)
   eventYear.append(year)






####@@@%%%****MAIN****%%%@@@####

# initializing the arrays for event details
eventName = []
eventMonth = []
eventDay = []
eventYear = []

# calling the main function to ask the user for event details
addEvent()

# prompt for if user wants to continue
prompt = input("Do you want to enter another event? NO to stop: ")

# while loop to keep asking for events until user enters 'NO'
while (prompt != "NO"):
   
   # repeat of what happened outside the loop
   addEvent()
   prompt = input("Do you want to enter another event? NO to stop: ")

# final function call to print the results
printEvents()