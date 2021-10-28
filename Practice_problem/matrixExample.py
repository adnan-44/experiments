"""
Program to print the matrix, where value of each element of ith row and jth column will be (ixj)
Input : X=3, Y=3
Ouptut :
1  2  3
2  4  6
3  6  9
"""

# Take row and column input from user
X = int(input("Enter X value : "))
Y = int(input("Enter X value : "))

# List to store the Matrix (list of list)
result = list()

# Outer loop for row
for i in range(X):
    # Inner loop for column
    row = list()
    for j in range(Y):
        row.append((i+1)*(j+1))
    
    # add the row in result
    result.append(row)

# Output - print the matrix
for row in result:
    # For each row, print the element with white spaces in a line
    for el in row:
        print(el, end="  ")

    # Break the line  
    print()
