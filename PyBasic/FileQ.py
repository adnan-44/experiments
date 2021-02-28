"""This code will read a line from file given by user"""
file = open(input('Enter filename to open: '),'r')
print("Starting pointer location in file is : ",file.tell())
print("Reading first line:")
print(file.readline())
print("Pointer location after reading first line is : ",file.tell())
file.close()
