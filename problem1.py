##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""

username = ""
password = ""

count = 0

while username != "admin" and password != "12345" and count < 3:
    username = input("Enter your username.")
    if username != "admin":
        print("Access denied")
        count = count + 1
    else:
        password = input("Enter your password.")
        if password != "12345":
            print("Access denied")
            count = count + 1
        else:
            print("Access granted")