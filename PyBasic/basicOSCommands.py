# Program to elustrate basic about os module
import os

os.rename('file1.txt','file3.txt')  # This will rename 'file1.txt' to 'file3.txt' in current directory
os.remove('file3.txt')              # This will remove 'file3.txt' file
os.mkdir('Example')                 # This will create a directory named "Example" in current directory
print('Your current dirctory',os.getcwd())                  # This will print path of current directory
os.chdir('Example')                 # This will change current directory to "Example"
os.mkdir("NewExample")
print('Your current dirctory',os.getcwd())
os.rmdir('NewExample')              # This will remove the directory called "NewExample" from current directory
