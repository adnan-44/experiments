# Program to create a class which has 2 methods getString and printString
# getString() method will be used to take input, and printString() to print the string

class Solution:
    # Method getString() to take input from user
    def getString(self):
        self.myString = input("Enter the input: ")

    # Method printString() to print string output
    def printString(self):
        print(self.myString)

# Create instance of class "Solution"
obj = Solution()

# Call the methods of Solution class using "obj" instance
obj.getString()
obj.printString()
