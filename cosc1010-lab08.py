# Your Name Here
# UWYO COSC 1010
# Submission Date
# Lab XX
# Lab Section:
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def string_converter(num):
    """checks and converts string to input or float"""
    isNeg = False
    if "-" in num:
        isNeg = True 
        num = num.replace("-", "")
    if "." in num:
        num_list = num.split(".")
        if len(num_list) == 2 and num[0].isdigit() and num_list[1].isdigit():
            if isNeg:
                return -1 * float(num)
            else:
                return float(num)
    elif num.isdigit():
        if isNeg:
            return -1 * int(num)
        else:
            return int(num)
    else:
        return False 
converted_number = string_converter(num= input("Please input a number "))
print(converted_number)




print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, x_lower, x_upper):
    """finds y for a range of x"""
    y_values = []
    for x in range(x_lower, x_upper + 1):
        y = m * x + b 
        y_values.append(y)
    return y_values

while True:
    m = input("Please type a value for m ")
    if m.lower() == "exit":
        break
    else:
        m = string_converter(m)
    b = input("Please type a value for b ")
    if b.lower() == "exit":
        break 
    else:
        b = string_converter(b)
    x_lower = input("Please type a value for the lower x bound ")
    if x_lower.lower() == "exit":
        break
    else:
        if "." in x_lower:
            print("please input a whole number")
            continue
        else:
            x_lower = string_converter(x_lower)
    x_upper = input("Please type a value for the upper x bound ")
    if x_upper.lower() == "exit":
        break 
    else:
        if "." in x_upper:
            print("please input a whole number")
            continue
        else:
            x_upper = string_converter(x_upper)
    if x_lower >= x_upper:
        print("The lower x bound may not be greater than the upper x bound")
        continue

            

    y_values = slope_intercept(m, b, x_lower, x_upper)
    print(y_values)

    




print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def square_root(num_1):
    """performs square root operation"""
    if "-" in num_1:
        return "null"
    sqrt = num_1 ** (1/2)
    return sqrt


def solve_quadratic(a, b, c):
    """solves quadratic formula for given inputs"""
    x_values = []
    x_1 = (-1 * b + square_root((b ** 2) - (4 * a * c))) / (2 * a)
    x_values.append(x_1)
    x_2 = (-1 * b - square_root((b ** 2) - (4 * a * c))) / (2 * a)
    x_values.append(x_2)

while True:
    a = input("please input an a value ")
    if a.lower == "exit":
        break
    

