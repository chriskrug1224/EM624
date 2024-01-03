"""
#----1----
# --Original code
N = input("Enter your characters: ")
L = []
for letters in N:
    letters.split()
    L.append(letters)
    print (L*4)

There is no reason to split letters. The for loop is already iterating through the input string one letter at a time.
Although not wrong necessarily, there is no reason to use a list as it adds unneeded complications
It is better to use a blank string as a starter and add to it the letters where needed. This also helps readability of the output for the user
This is also printing the list itself 4 times, not the letters. Each for loop iterations adds the first letter, prints the new list four times,
adds the second letter, prints the new list four times, etc. It doesn't add each letter four times for one output like desired.
My solution is as follows:
"""


N = input("Enter your characters: ")
output = ""
for letters in N:
    output += letters * 4
print(output)



#----2----
# --Original code
"""
while True:
    #prompts and receives user input
    char = input('Please enter an alphabetical character:')
    if len(char) > 1: #checks if input is more than one character
        print ('Invalid input')
    else:
        if char == 'a' or 'e' or 'i' or 'o' or 'u' or 'y': #checks if input is a vowel
            print ('False')
    else:
        print ('True')
"""
"""
I am unable to atleast run the code. What I see wrong is a few things:
It should not have two else statements, the first else when checking for a vowel should use an elif statement in some way or be a nestive else statement
It is also really only checking to see if char is equal to 'a.' To check for all vowels, it should have explicity written if char == a, char == e, etc.
There is also no way to break out of the while loop. 
It also does not check for captial letters, only lower case
My solution is as follows:
"""
while True:
    char = input("Please enter an alphabetical character:")
    if len(char) > 1:
        print("Invalid input")
    else:
        char = char.lower()
        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "y":
            print("False")
        else:
            print("True")
            break
