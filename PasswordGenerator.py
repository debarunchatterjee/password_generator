import random as rd
import string 

print("Welcome to Password Generator",end="\n")
passFormat=int(input("For Alphabetical Password press 1, for Numeric Pin press 2 and for Alphanumeric Password press 3 "))
passLength=int(input("Enter the length of your desired password (Number of characters) "))
passString=""
characters="!@#$_%&?" #We can also use string.punctuation. It is avoided here for unnecessary characters. 

if(passFormat==1):
    for i in range(passLength):
        passString+=rd.choice(string.ascii_letters)
    print("\nYour randomly generated password is:",passString)
    
elif(passFormat==2):
    for i in range(passLength):
        passString+=rd.choice(string.digits) #We can also use rd.randint(0,9)
    print("\nYour randomly generated PIN is:",passString)
    
elif(passFormat==3):
    secondChoice=input("Do you want characters in your password, Y/N? ")
    secondChoice=secondChoice.upper()
    if (secondChoice=="N"):
        for i in range(passLength):
            passString+=rd.choice(string.ascii_letters+string.digits)
            '''
            The following block of code ensures that the generated password
            will have at least one digit. (To make the password truly alphanumeric).
            passList=list(passString)
            position=rd.randint(0,passLength-1)
            passList.pop(position)
            passList.insert(position,rd.choice(string.digits))
            passString="".join(passList)
            
            '''
        print("\nYour randomly generated Password is:",passString)
    elif (secondChoice=="Y"):
        for i in range(passLength):
            passString+=rd.choice(string.ascii_letters+string.digits+characters)
        '''
        The following block of code ensures that the generated password
        does not start with a character since a lot of accounts do not allow
        passwords to begin with a character.
        
        '''
        passList=list(passString)
        passList.pop(0)
        passList.insert(0,rd.choice(string.ascii_letters+string.digits))
        if(passLength>=2):
            position=rd.randint(1,passLength-1)
            passList.pop(position)
            passList.insert(position,rd.choice(characters))
            passString="".join(passList)
            
        print("\nYour randomly generated Password is:",passString)
else:
    print("\nYour choice of password type is invalid, please choose 1,2 or 3")