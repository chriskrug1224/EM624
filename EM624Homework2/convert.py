# Christopher Kruger
while True:
    tempCelsius = input("What is the temperature in Celsuis you want to convert? \n Type the value or 'done' to exit\n")
    if tempCelsius == 'done':
        print("\n Thanks for using the tool!\n")
        break
    try:
        x = float(tempCelsius)
    except ValueError:
        print("\n Wrong input, please only input Numbers!\n")

    tempFahrenheit = (float(tempCelsius) * 1.8) + 32
    print("\n The equivalent of ", tempCelsius, " degree Celsius is ", tempFahrenheit, " Fahrenheit\n")