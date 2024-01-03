# Author: Christopher Kruger
# SSW540: Celsius/Fahrenheit Conversion
Fahr = float(input("What is the temperature you would like to convert from Fahrenheit to Celsius?\n"))
Cels = round((Fahr - 32) * (5/9))
print("The conversion from", Fahr, "F to Celsius is:", Cels, "C")