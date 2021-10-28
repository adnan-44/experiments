# Program to find the number which are divisible of 7 but not multiple of 5 in a given range

start = int(input("start? "))
end = int(input("End ? "))

for number in range(start, end+1):
    if number%7 == 0 and number%5 != 0:
        print(number,", ", end="")
