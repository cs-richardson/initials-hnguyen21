'''
This program takes a name as an input and prints the initials of the name.
As long as there are any amount of spaces
between first names, middles names and last names, the code will work.
By: Ben
'''

def initials(name):
    fullInitials = ""
    seperatedNames = name.split()
    
    for n in seperatedNames:
        fullInitials = fullInitials + n[0].upper()

    print(fullInitials)
        
fullName = input("")
initials(fullName)
