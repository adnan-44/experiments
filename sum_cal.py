print('This is first Pyhton program')
i = 0
while(True):
	print('Enter a number')
	num = input()
	if num == 'no':
		print('done ')
		print('Total sum is',i)
		print('Task executed......')
		exit()
	i = i+int(num)
