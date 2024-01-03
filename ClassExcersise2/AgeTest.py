name = input("What is your name? \n")
age = input("How many years old are you?\n")
currentYear = 2023
ageMinusHundred = 100 - int(age)
newYear = 2023 + ageMinusHundred
print("Hi, " + name + "! You will be 100 in the year", newYear)
print("Only another", (ageMinusHundred*365), "days!")
