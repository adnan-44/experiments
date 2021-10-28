# Program to calculate the factorial of given number
# Factorial of 3 => 1 x 2 x 3 = 6 

# Take number input from user
number = int(input('Enter a number : '))

# Set default factorial as 1 (Because 1 is identity for multiplication)
fact = 1

# Iterate 'number' times, and in each iteration multiply number to the fact
for i in range(1, number+1):
    fact *= i

print(fact) # Output
