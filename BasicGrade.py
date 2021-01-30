#Basic code calculate Grade
n = int(input('Enter number of subjects: '))
marks = 0
for i in range(0,n):
	print(i+1,end=" ")
	marks += int(input(' subject marks: '))

per = marks/(n*100) * 100
Grade = ''
if per >= 90 and per <= 100 :
	Grade = 'A+'
elif per >= 80 and per < 90 :
	Grade = 'A'
elif per >= 70 and per < 80 :
	Grade = 'B+'
elif per >= 60 and per < 70 :
	Grade = 'B'
elif per >= 50 and per < 60 :
	Grade = 'C+'
elif per >= 40 and per < 50 :
	Grade = 'C'
elif per >= 35 and per < 40 :
	Grade = 'D'
elif per < 35:
	Grade = 'F'

print('Grade : '+Grade)
print('Total percentage '+ str(per)+ '%')
