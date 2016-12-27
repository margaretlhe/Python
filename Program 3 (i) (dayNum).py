#dayNum.py
#This program takes a given date and calculates the day number of the year
#by Margaret He, ECS 10, Fall Quarter 2013

def dayNum():
    month = input("Input a month. Spell it out completely, and capitalize the first letter ")
    day = eval(input("Input a day "))
    year = eval(input("Input a year "))
    
    print("Your input: ", month, day,",", year)

#determine if the year is a leap year
    if year % 400 == 0:
          leapyear = 1          
    elif year % 100 == 0:
          leapyear = 0          
    elif year % 4 == 0:
          leapyear = 1
    else:
          leapyear = 0

    if (leapyear == 1):
          print(year, "is a leap year")
    if (leapyear == 0):
          print(year, "is not a leap year")

#determine if the date is a valid day
#first take care of the special case of February
    if (month == 'February'):
        if (day >= 1) and (day < 29):
            valid = 1
        elif (day == 29):
            if (leapyear) == 1:
                valid = 1
            else:
                valid = 0
                print("Sorry, this day is inapplicable for the month of February.")

#Next, take care of all the other months
    else:
        if (day <= 31) and (day >= 1) and (month == 'January') or (month == 'March') or (month == 'April') or (month == 'May') or (month == 'June') or (month == 'July') or (month == 'August') or (month == 'September') or (month == 'October') or (month == 'November') or (month == 'December'):
            valid = 1
        elif (day <= 30) and (day >= 1) and (month == 'April') or (month == 'June') or (month == 'September') or (month == 'November'):
            valid = 1
            
        else:
            valid = 0
            
    if (valid == 1):
        print(month, day,",", year, "is a valid date")
    else:
        print(month, day,",", year, "is not a valid date")
    
#This simply converts the name of a month to the number of the month
    MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    
    for i in range(12):
        if (MONTHS[i] == month):
            print("Month", month, "is month", i+1)

#The following converts the day of the month to the day of the year
            if (valid == 1):
                if (i <= 1):
                    dayNum = (31 * i) + day
                    print(month, day,",", year, "is day number", dayNum, "of this year")
                elif (leapyear == 0) and (i > 1):
                    dayNum = (31 * i) + day
                    dayNum = dayNum - ((4*(i+1) + 23)//10)
                    print(month, day,",", year, "is day number", dayNum, "of this year")

                elif (leapyear == 1) and (i > 1):
                    dayNum = (31 * i) + day
                    dayNum = dayNum - ((4*(i+1) + 23)//10) + 1
                    print(month, day,",", year, "is day number", dayNum, "of this year")



dayNum()


