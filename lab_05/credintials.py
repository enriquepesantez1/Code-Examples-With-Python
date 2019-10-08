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
     return uname.lower()


# Function that finds the user password and checks the length
def userPassword():
    # ask user to create a new password
    passwd = input("Create a new password: ")
    userPwdStrength(passwd)



#Function Checks if the User Password is strong
def userPwdStrength(passw):
    numLower = 0
    numUpper = 0
    # TODO modify this to ensure the password has at least 8 characters
    for i in range(len(passw)):
        if passw[i].islower() == True:
            numLower = numLower + 1
        if passw[i].isupper() == True:
            numUpper = numUpper + 1
    while len(passw) <= 8 or numUpper == 0 or numLower == 0:
        print("Fool of a Took! That password is feeblie!")
        passw = input("Create a new password: ")
        return passw
    if len(passw) <= 10:
        print('Your password is weak')
    else:
        print('Your Password is Strong')
    


def main():
    name = UserName()
    uname1 = MaristStyle(name)
    userPassword()
    input("Press Enter to Configure your account ")
    print("The force is strong in this one....")
    print("Account configured. Your new email adress is: " + uname1 + "@marist.edu")


main()