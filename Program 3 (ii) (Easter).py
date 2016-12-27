#Easter.py
#This program computes the Easter date in the years within 1900-2099
#by Margaret He, ECS 10, Fall Quarter 2013

def Easter():
    year = eval(input("What year would you like to calculate Easter?\n(Please choose a year that falls within 1900-2099): "))

#Make sure year is an integer value

    year = int(year)

#Check to see if the year falls in the correct range   

    if (year >= 1900) and (year <= 2099):
        valid = 1
        print("\nGreat, the year you selected falls in the appropriate range!")
    else:
        valid = 0
        print("\nUnfortunately, the year you selected is invalid")

#Define the variables
        
    a = year % 19
    b = year % 4
    c = year % 7
    d = (19 * a + 24) % 30
    e = (2* b + 4 * c + 6 * d + 5) % 7


#Calculate the day number for Easter

    if (valid == 1):
        if (year != 1954) and (year != 1981) and (year != 2049) and (year != 2076):
            day = 22 + d + e

        elif (year == 1954) or (year == 1981) or (year == 2049) or (year == 2076):
            d = d - 7
            day = 15 + d + e
            
#Determine Easter date: 
            
        if (day <= 31):
            month = 'March'
            print("In the year of", year, "Easter falls on March", day)

        elif (day > 31):
            month = 'April'
            day = d + e - 9
            print("In the year of", year, "Easter falls on April", day)
    
Easter()
