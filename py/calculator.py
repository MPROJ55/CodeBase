import math 
first_digit = input("First Digit? ")
Second_digit = input("second digit? ")
order_of_operation = input("What order of operation? (+,*,/,-)")

if order_of_operation == "+":
    result = first_digit + Second_digit

elif order_of_operation == "-":
    result = first_digit - Second_digit
elif order_of_operation == "*":
    result = first_digit * Second_digit
elif order_of_operation == "/":
    result = first_digit / Second_digit
else:
    print("Could not calculate result ")
