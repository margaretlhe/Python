#Student database.py
#by Margaret He, ECS 10, Fall Quarter 2013

#Identify the dictionaries
name = {}
ID = {}
major = {} #Indexes are majors/Keys are ID numbers
Major = {} #Indexes are Majors/Keys are student names
work = {}

#Incorporate lists (Holds the Values)
namelist = []
IDlist = []
majorlist = []
Major_names = []
major_IDs = []
worklist = []


#Open File
infile = open("database.txt", 'r') 
outfile = open("newdatabase.txt", 'w')

lines = infile.readlines() #Reads the lines from a file

def Read_Set(): #Sets up dictionaries
    for line in lines:
        line = line.strip() #Puts lines into a list and eliminates white space
        category = line.split('; ') #Separates the fields in each line
        categories = list(category) #Inputs the categories into a list
        for i in range(len(category)):
            category[i] = category[i].strip()
        
#Name Dictionary Setup: {(lastname, firstname), student's info}
        student_name = categories[0]
        student_info = categories[1] + "; " + categories[2] + "; " + categories[3] + "; " + categories[4] + "; " + categories[5]
        name[student_name] = student_info #Create new dictionary entry
        namelist.append(student_info) #Append the student names (keys) into namelist

#ID Dictionary Setup: {student's ID #, student's info}
        ID_num = categories[1]
        ID_info = categories[0] + "; " + categories[2] + "; " + categories[3] + "; " + categories[4] + "; " + categories[5]
        ID[ID_num] = ID_info #Create new dictionary entry
        IDlist.append(ID_info) #Append the ID nums (keys) into IDlist

#Major Dictionary Setup: {Major, student's ID #} <-- (students with that major)
        major_name = categories[3]  

        if major_name in major: #If there is a major name already in the major dictionary, continue adding student names 
            major[major_name].append(ID_num) #Append the ID_num (value) into the dictionary [key]
            major_IDs.append(ID_num) #Add one student ID # (per major) to the major_IDs list
            Major[major_name].append(student_name) #Append each student name to its corresponding major key
            Major_names.append(student_name) #Add one student name (per major) to the major_names list
            
        else: #In the beginning, since major dictionary is empty, you start with the else statement
            major[major_name] = [ID_num] #Create new dictionary entry (1)
            major_IDs.append(ID_num) #Add one student ID # (per major) to the major_IDs list
            Major[major_name] = [student_name] #Create new dictionary entry (1)
            Major_names.append(student_name) #Add one student name (per major) to the major_names list
            majorlist.append(major_name)
            

#Work Dictionary Setup: {Weekly work hours, student's ID #} <-- (students working that # of hours)
        work_hours = categories[5]

        if work_hours in work: #If the work hours is already put into the work dictionary
            work[work_hours].append(ID_num) #Append the ID # (value) ino the dictionary
            worklist.append(ID_num) #Add each ID # into the Work IDs list

        else:
            work[work_hours] = [ID_num] #Create new dictionary entry
            worklist.append(ID_num) #Append each person's work hours to the work list

    return name, ID, major, namelist, IDlist, Major_names #Return Dictionaries so we can call them later



def Sort_Print(name, ID, major, namelist, IDlist, Major_names): #Print out the dictionaries in alphabetical/chronological order
#Name Dictionary
    studentkeys = name.keys()
    namelist = list(studentkeys)

    namelist.sort()
    for student_key in namelist: #For each name in name list
        student_value = name[student_key] #Assigns the value to student_value
        print(student_key, ":", student_value) #Print key followed by value

    print("\n")

#ID Dictionary
    IDkeys = ID.keys() #Stores the dictionary's keys
    IDlist = list(IDkeys) #Puts all the keys (ID #'s) in ID list

    IDlist.sort() #Sorts it in chronological order
    for ID_key in IDlist: #For each ID # in ID list
        ID_value = ID[ID_key] #Generates value from Dictionary[key]
        print(ID_key, ":", ID_value) #Print key followed by value

    print("\n")
    
#Major Dictionary
    Majorkeys = Major.keys() #Stores the dictionary's keys
    majorlist = list(Majorkeys)#Puts all the keys (majors) in major list
    majorlist.sort() #Sorts it in chronological order
    
    for major_key in majorlist: #For each major in major list
        Major_value = Major[major_key] #Generate values from dictionary[key]
        Major_value.sort() #Put the student names in alphabetical order
        print(major_key, ":", '; '.join(Major_value))


def query_1(major, ID): #Computes the average GPA for all students of a particular major
    print("Here are the majors the students have:", ', '.join(majorlist))
    majorchoice = input("Choose a major from the list above to calculate its average GPA: ")
    majorchoice = majorchoice.title()
  
    if majorchoice in majorlist: #If the user enters a major from the list
        totalGPA = 0
        num_students = 0
        for id_num in list(major[majorchoice]): #For each id number in each major's ID num list
            id_info = ID[id_num] #ID dictionary's value string
            category = id_info.split("; ")
            GPA = eval(category[3]) 
            totalGPA += GPA
            num_students += 1
            avgGPA = totalGPA /num_students
        print("The average GPA for that particular major is:", avgGPA)

    else:
        print("\nYou did not enter a valid major.")
        

def query_2(major, ID): #Computes the average # of hours worked by all students with a particular major
    print("Here are the majors the students have:", ', '.join(majorlist))
    majorchoice = input("Choose a major from the list above to calculate its average GPA: ")
    majorchoice = majorchoice.title()
    if majorchoice in majorlist:
        totalwork = 0
        num_students = 0
        for id_num in list(major[majorchoice]): #For each id number in each major's ID num list
            id_info = ID[id_num] #ID dictionary's value string
            category = id_info.split("; ")
            workhours = eval(category[4])
            totalwork += workhours
            num_students += 1
            avghours = totalwork /num_students
        print("The average number of hours worked by all students with that particular major is:", avghours)

    else:
        print("\nYou did not enter a valid major. Try again.") 
           

def query_3(work, ID): #Computes the average GPA of all students who work more than X hours per week
    workhours = work.keys()
    workhours = list(workhours)
    
    try: 
        X = eval(input("To calculate the average GPA of all students who work more than X number of hours per week, \nEnter a number for X: "))
        totalGPA = 0
        num_students = 0
        for i in workhours: #For each student's work hours
            if (eval(i) > X):
                 for id_num in list(work[i]): #For each id number in each major's ID num list
                     id_info = ID[id_num] #ID dictionary's value string
                     category = id_info.split("; ")
                     totalGPA += eval(category[3])
                     num_students += 1
                     avgGPA = totalGPA / num_students
        print("The average GPA for students who work more than,", X, "hours is: ", avgGPA)
                     
    except:
        print("You did not enter a valid input.")
     
       
def Menu(): #Answers Queries
    print("Which of the following would you like the program to compute?")
    print("1) Compute the average GPA for all students with a particular major")
    print("2) Compute the average # of hours worked of all students with a particular major") 
    print("3) Compute the average GPA of all students who work more than X hours per week")

   
#Main Program
Read_Set() 
Sort_Print(name, ID, major, namelist, IDlist, major_IDs)
print("\n")
Menu()

myquery = True
while myquery == True:
    query_num = input("\nChoose the corresponding # to the menu(Or press any other key to quit): ")

    if query_num == "1":
        query_1(major, ID)
    
    elif query_num == "2":
        query_2(major, ID)
        
    elif query_num == "3":
        query_3(work, ID)
        
    else:
        myquery = False

print("Thank you for using this software. Goodbye.")
infile.close()
outfile.close()


            
