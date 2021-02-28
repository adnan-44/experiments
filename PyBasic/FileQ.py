"""This code will read all lines from file given by user"""
file = open(input('Enter filename to open: '),'r')
print("Starting pointer location in file is : ",file.tell())
print("Lines in file are :")
for lines in file:
    print(lines)
print("Pointer location after reading lines is : ",file.tell())
file.close()
