def main():
    num1 = 10
    num2 = 3

    add_result = add_numbers(num1, num2)
    subtract_result = subtract_numbers(num1, num2)
    multiply_result = multiply_numbers(num1, num2)
    divide_result = divide_numbers(num1, num2)

    # Correct results for each operation
    display_results(num1, "+", num2, "=", add_result)
    display_results(num1, "-", num2, "=", subtract_result)
    display_results(num1, "*", num2, "=", multiply_result)
    display_results(num1, "/", num2, "=", divide_result)

def add_numbers(mynum1, mynum2):
    my_add_result = mynum1 + mynum2
    return my_add_result

def subtract_numbers(mynum1, mynum2):
    my_subtract_result = mynum1 - mynum2
    return my_subtract_result

def multiply_numbers(mynum1, mynum2):
    return mynum1 * mynum2

def divide_numbers(mynum1, mynum2):
    my_divide_result = mynum1 / mynum2
    return my_divide_result 

def display_results(mynum1, operator, mynum2, equals, my_equals):
    # Check if result is integer or float and display accordingly
    if isinstance(my_equals, int):
        print(f'{mynum1} {operator} {mynum2} {equals} {my_equals}')
    else:
        print(f'{mynum1} {operator} {mynum2} {equals} {my_equals:.3f}')

if __name__ == '__main__':
    main()

