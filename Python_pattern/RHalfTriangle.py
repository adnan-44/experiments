#This code will print half-triangle patern
num = int(input('Enter a number: '))
for i in range(0,num):
	for j in range(0,i):
		print(i,end=" ")
	print()
