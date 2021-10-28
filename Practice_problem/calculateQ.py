"""
Program to take comma separated numbers input, and calculate the value of "Q" for each number
Use the number as "D" for equation
Equation : Q = Square root of ((2*C*D)/H), where C=50 and H=30, round off the result also

Input : 10,23,33
Output : [5,8,10]
"""

import math

# Take input from user
comma_input = input("Enter comma separated numbers: ")

# List to store the numbers get from input, and another list for result
input_numbers = list()
answers = list()

# Split the input string from "," and get/set number into input_numbers list
for number in comma_input.split(","):
    input_numbers.append(int(number))

# Iterate the number list
for number in input_numbers:
    # For each number in list, calculate value of Q, and add the round-off result in asnwers's list
    Q = math.sqrt(2*50*number/30)
    answers.append(int(Q))  # To round off the number

print(answers) # Output
