# Author: Christopher Kruger
# Homework 2
# This program prompts the user to input a password until they specify 'done.'
# While they are inputting their password, the program will
# check to see if it matches a minimum length of 5, a max length
# of 12, any combination of numerical and alphabetical characters,
# and the word 'password' must not be in it.
print ("Please input a password that matches the following requirements: \n ")
print ("Minimum Length = 5 \n")
print ("Maximum Length = 12 \n")
print ("Any combination of numerical and alphabetical characters (case insensitive) \n")
print ("The word 'password' must not be in it \n")
while True:
    # Getting the password input value
    passwordInput = input("Please input your password following the stated requirements or type 'done': \n")
    # Checks to see if program needs to terminate
    if passwordInput == 'done':
        print("Thanks for using my tool! \n")
        break
    # Checks to see if the password meets the minimum length
    elif len(passwordInput) < 5:
        print("Error: The password is less than 5 characters!\n")
    # Checks to see if the password meets the maximum length
    elif len(passwordInput) > 12:
        print("Error: The password is greater than 12 characters!\n")
    # Checks to see if the password has no spaces and has numerical and alphabetical characters
    elif not passwordInput.isalnum():
        print("Error: The password contains non-alphanumerical characters!\n")
    # Checks to see if the word 'password' is contained
    elif 'password' in passwordInput.lower():
        print("Error: The word 'password' is contained!\n")
    # Password is successful!
    else:
        print("Your password has been accepted!")