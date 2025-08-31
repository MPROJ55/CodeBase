import random

print("\n Task 1. Import a function")
integer = random.randint(0, 100)
print("A random int between 0 and 100 is", integer)

print("\n Task 2. See the help.")
print("If you want to see a function's documentation, enter")
print("help followed by the function name.")


print("\n Task 3. Basic function without the parameters and arguments")
def my_function():
    location = "We are inside of my function."
    print(location)

print("Before calling my_function.")
my_function()
print("After calling my function.")

print("\n Task 4. Basic function that has a docstring and the keyword pass")
def my_empty_function():
    # incomplete function uses pass
    pass
print("\n Task 5  Positional Arguments require same qty of arguments and \ parameters in the same order representing the same data types.")
def water(qty, h2o, price):
    print(f'{qty} {h2o} cost ${price:.2f}')
print('Call 1:')
water(1, "Aquafina" , 2.69)
print('Call 2 throws an error bc we passed only 2 arguments.')
print('Call 3 does not throw error but is logically incorrect')
water("nestle pure water" , 2.69, 1)

print("\n Task 6. Keyword Arguments allow flexibility")
def water_keywords(qty, h20, price):
    print(f' {qty} {h20} cost ${price:.2f}')
print("\n Call 1. You must supply parameters")
print("\n Call 2. Keyword arguments in the same order as the function def. ")
water_keywords(qty=2, h20="Aquafina", price=2.69)
print("\n Call 3. Keyword arguments Not in the the order of the funciton def.")