""" This code will create new files with given names.
    We'll need names.txt file (which will contain one name per line) and
    body.txt (which will contain body text of message) """

names_file = open('names.txt','r')

for name in names_file:
    body = open('body.txt','r')
    new_file = open(name.strip()+".txt",'x')
    content = "Hello " + name.strip() + " \n"
    for lines in body:
        content += lines
    new_file.write(content)

print('Files created successfully')
