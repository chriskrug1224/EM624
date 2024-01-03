def factorial(num):
    if num < 0:
        return 0
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        while (num > 1):
            fact *= num
            num -= 1
        return fact

def floating(num1, num2):
    return float(-num2/num1)

num = float(input("Please input a number that you would like to find the factorial of:\n"))
num1 = float(input("Please input the number for a that you would like for solving the floating value in a*x + b = 0\n"))
num2 = float(input("Please input the number for b that you would like for solving the floating value in a*x + b = 0\n"))

print(factorial(num))
print(floating(num1, num2))