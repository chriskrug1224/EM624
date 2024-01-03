'''
A website requires the users to input username and password to register.

Write a program to check the validity of passwords input by users.

The following are the criteria for checking the password:

At least 1 letter between [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
At least 1 number between [0,1 2, 3, 4, 5, 6, 7, 8, 9]
At least 1 letter between [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
At least 1 character from [$, #, @]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of any number of comma separated passwords and will check them according to the above criteria. Use a validation function to check the passwords.

Passwords that match the criteria will be printed, each separated by a comma and a space.



Example

If the following passwords are given as input to the program:

ABd1234@1,a F1#,2w3E*,2We3345

Then, the output of the program should be:

The following are the passwords that have been accepted:

ABd1234@1
'''
def is_valid_password(password):
    if 6 <= len(password) <= 12:
        has_lowercase = False
        has_uppercase = False
        has_digit = False
        has_special_char = False

        special_chars = "$#@"

        for char in password:
            if char.islower():
                has_lowercase = True
            elif char.isupper():
                has_uppercase = True
            elif char.isdigit():
                has_digit = True
            elif char in special_chars:
                has_special_char = True

            if has_lowercase and has_uppercase and has_digit and has_special_char:
                return True

    return False

# Input: Comma-separated passwords
input_passwords = input("Enter passwords separated by commas: ")
passwords = input_passwords.split(',')

valid_passwords = []

for password in passwords:
    password = password.strip()
    if is_valid_password(password):
        valid_passwords.append(password)

if valid_passwords:
    print("The following are the passwords that have been accepted:")
    print(", ".join(valid_passwords))
else:
    print("No valid passwords found.")
