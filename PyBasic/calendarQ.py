#This code will print calendar according to given month using Python library
import calendar

#taking input of year and moth from user
year = int(input("Enter Year : "))
month = int(input("Enter Month : "))
print("\n"+calendar.month(year, month))
