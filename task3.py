#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

number = -1

while number != int(number) or number%2 != 0:
    number = float(input("Please enter a number. "))
    if number%2 == 0 and int(number):
        print("That is an even integer.")
    else:
        print("That is not an even integer.")