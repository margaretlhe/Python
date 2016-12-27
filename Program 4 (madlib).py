#madlib.py
#Program 4 by Margaret He, ECS 10, Fall Quarter 2013

def madlib():
    print("This program creates a story from a text in a file.")    

#First, ask the user what files they want to open

    origfileName = input("What file do you want to read from? ")
    newfileName = input("What file do you want to write to? ")
    
#Open the files

    origfile = open(origfileName, "r")
    newfile = open(newfileName, "w")
    
#Read the orgiinal file and split it into words

    data = origfile.read()    
    origfile.close()
    new_story = ""
    Words = data.split()
    keys = []
    for i in Words:
        if (["NB", "NS", "NP", "AJ", "AV", "NM", "VB", "VP"] == i[:2]):
           keys.append()
           print(keys) 
            
#Move those words into New Keys

    new_keys = []
    for k in Words:
        if (k[:2] == "NB"):
            n = input("Please input a number: ")
            new_keys.append(n)
        if (k[:2] == "NS"):
            n = input("Please input a singular noun: ")
            new_keys.append(n)
        if (k[:2] == "NP"):
            n = input("Please input a plural noun: ")
            new_keys.append(n)
        if (k[:2] == "AJ"):
            n = input("Please input an adjective: ")
            new_keys.append(n)
        if (k[:2] == "AV"):
            n = input("Please input an adverb: ")
            new_keys.append(n)
        if (k[:2] == "NM"):
            n = input("Please input a person's name ")
            new_keys.append(n)
        if (k[:2] == "VB"):
            n = input("Please input a verb: ")
            new_keys.append(n)
        if (k[:2] == "VP"):
            n = input("Please input a verb in past-tense: ")
            new_keys.append(n)

    print("\n")
    print(new_keys)
    
#Print new madlib story

    print("\nThe madlib story:")
    template_word = 0
    
    for p in Words:
        if p[:2] in ['NB', 'NS', 'NP', 'AJ', 'AV', 'NM', 'VB', 'VP']:
            new_story = new_story + " " + new_keys[template_word]+p[2:]
            template_word = template_word + 1
        else:
            new_story = new_story + " " + p
    print(new_story)
    
#Close and save the file
    
    print(new_story, file=newfile)
    newfile.close()

madlib()
