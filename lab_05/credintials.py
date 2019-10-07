# CMPT 120 Intro to Programming
# Lab # 5 - Working with Strings and Functions
# Aurthor: Enrique Pesantez
# Created: 2019-10-03



#Function gets the Users First and Last Name
def UserName():
    # get user's first and last names
    first = input("Enter your fist name: ")
    last = input("Enter your last name: ")
    return first, last

#Function edits the names to Marist Style
def MaristStyle(name):
    # TODO modfiy this to generat a Marist-style username
     uname = name[0] + "_" +  name[1] + "1"
     return uname

# Function that finds the user password
def userPassword():
    # ask user to create a new password
    passwd = input("Create a new password: ")

    # TODO modify this to ensure the password has at least 8 characters
    while len(passwd) <= 8:
        print("Fool of a Took! That password is feeblie!")
        passwd = input("Create a new password: ")
    return passwd
    

def main():
    name = UserName()
    uname1 = MaristStyle(name)
    pwd = userPassword()
    print("The force is strong in this one....")
    print("Account configured. Your new email adress is: " + uname1 + "@marist.edu")

main()