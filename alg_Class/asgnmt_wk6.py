#This week's assignment involves writing a Python program to determine
#whether a password exactly meets the following requirements for a secure
#password:

#the length of the password must be greater than some minimum length and
#less than some maximum. You should decide on the minimum (at least 6)
#and maximum (at least 15) allowable lengths; it must not include any spaces;
#it must contain at least one digit; and it must contain at least one
#alphabetic character. Your program must contain at least three functions:

#one function to check that the password is the proper length;
#a second function to check whether it contains the required number of
#characters/digits (Hint: to determine whether it contains at least one
#digit and one alphabetic character, use a loop and the isalpha or isdigit
#methods); and a third function to verify that it does not contain the
#prohibited character (space). Your program should prompt the user for the
#candidate password and then each function and display either that the
#password is valid or the first reason it is invalid. 

#You cannot use Regular Expressions (RE) !


#FUNCTIONS----------------------------------------------------------------
#password request with explanation
def getPass():
    print("Create your personal password. The requirements are as follows: ")
    print("- min length of 7 chars")
    print("- max length of 21 chars")
    print("- at least one alpha character")
    print("- at least one numeric digit\n")
    print("enter your password:")
    password = input()
    return password

#brief request to reduce wordage during recursive requests
def getPAss2():
    password = input("7-21 length password with numbers and letters: \n")
    
#main checking function with sub-functions within and some flavor to make it more personal
def passwordCheck(val, cond1, cond2, cond3):
    print("Validating password:")
    print(".")
    print("..")
    print("...")
    #run checks
    checkLength(val, cond1)
    checkDigits(val, cond2)
    checkAlpha(val, cond3)
    print(cond1, cond2, cond3)
    #respond to checks
    if (cond1 == False):
        print("Length is too short or too long (7-21 character range)")
    if(cond2 == False):
        print("There must be at least one letter in your password")
    if (cond3 == False):
        print("There must be at least one number in your password")
    if (cond1, cond2, cond3 == True):
        print("your password is valid")
        print("Would you like to try another password?")
        response = input()
        if (response == 'y'.lower() or 'yes'.lower()):
            main()
        else:
            print("Good bye")
            

#check for any spaces and return a version of the password without them
def spaceCheck(word):
    newPass = ""
    word = word.strip()
    for letter in word:
        if (letter != " "):
            newPass = newPass + letter

    return word
            

def checkLength(val, cond):
    print("length:", len(val))
    if (len(val) < 7 or len(val) > 21):
        print("cond:", cond)
        print("Your password length must range from 7 through 21.")
    else:
        cond = True
        print("cond:", cond)

def checkDigits(val, cond):
    count = 0
    for letter in val:
        if (letter.isalpha()):
            count = count+1
    if (count < 1):
        print("- at least one alpha character")
    else:
        cond = True

def checkAlpha(val, cond):
    count = 0
    for letter in val:
        if (letter.isdigit()):
            count = count+1
    if (count < 1):
        print("- at least one numeric digit")
    else:
        cond = True
    


def main():
#MAIN---------------------------------------------------------------------
#CONSTANTS
    #values used to direct program behavior based on whether or not conditions being met are true or false
    check1 = False
    check2 = False
    check3 = False


#Body----------------------------------------------------------------

    password = getPass()
    print(password)
    print(len(password))
    password = spaceCheck(password)
    print(password)
    passwordCheck(password, check1, check2, check3)

#Execution----------------------------------------------------------------
main()
