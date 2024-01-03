#Christopher Kruger
# option = input("Did you want to check your number if it is even/odd (type 1), or the year you will turn 100 (type 2)?\n")
# if option == 1:
while True:
    choice1 = input("What number do you want to check? Or type 'done' to quit \n")
    if choice1 == 'done':
        print("\nThanks for using the tool!\n")
        break
    else:
        choice1 = int(choice1)
        if choice1 % 4 == 0:
            print("\nYour number is even, and divisible by four!\n")
        elif choice1 % 2 != 0:
            print("\nYour number is odd!\n")
        elif choice1 %2 == 0:
            print("\nYour number is even!\n")
