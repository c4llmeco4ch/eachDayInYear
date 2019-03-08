#see attached jpg

'''
* @param day The day of the month we want to print
* @param month The string of the month we want to print
*        i.e. "Jan"
* Given a "day" and "month", this function prints out
* The associated calendar day. So, passing 1 and "Feb"
* Prints "Feb 1st"
'''
def printDay(day, month):
  ending = ""
  if day == 1 or (day >= 20 and 
                          day % 10 == 1):
    ending = "st"
  elif day % 10 == 2 and (day > 20 or                                               day < 10):
    ending = "nd"
  elif day % 10 == 3 and (day > 20 or day < 10):
    ending = "rd"
  else:
    ending = "th"
  print(month + " " + str(day)
        + ending)

'''
* Goal: For all the days in the year, we want to
* print out the calendar day associated with that day in 
* the year
* For example, the 32nd day of the year is Feb 1st
'''

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
  "Aug", "Sep", "Oct", "Nov", "Dec"]
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, +
                  30, 31]
currentMonth = 0
runningTotal = 0
DEBUG = False

for day in range(1,366):
  if day > runningTotal + daysInMonth[currentMonth]:
    runningTotal += daysInMonth[currentMonth]
    currentMonth += 1
    if DEBUG:
      print("Moving to " + months[currentMonth])
  printDay(day - runningTotal, months[currentMonth])
