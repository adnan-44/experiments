# Program to create dictionary of where data should be like {1:1, 2:4, 3:9}

# Take number input from the user
number = int(input('Enter a number : '))

# Create an empty dictionary to store the result
series = dict()

# Now loop 'number' times
for i in range(1, number+1):
    # In each iteration, set i as key, and i times i as value (i*i)
    series[i] = i*i

print(series)   # Output
