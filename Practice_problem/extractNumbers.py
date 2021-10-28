""" 
Program to take comma "," separated input then create a list and a tuple from it.
Example input => 12,43,57,86
output => [12,43,57,86]
          (12,43,57,86)
"""

# Take input from user
comma_input = input("Enter comma separated number: ")

# Create an empty list to store values
numbers_list = list()

# split the given input string on "," and add them to list
for number in comma_input.split(","):
    numbers_list.append(int(number)) # convert number to int type and add to numebrs_list

numbers_tuple = tuple(numbers_list)     # create tuple with the help of list

# Output
print("List :", numbers_list)
print("Tuple :", numbers_tuple)
