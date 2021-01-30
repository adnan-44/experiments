#Code to print fibonaci series
n = int(input('Enter range: '))
a = 0
b = 1
print('\nFibonaci series:')
print(a)
print(b)
for i in range(n):
   c = a+b
   print(c)
   a = b
   b = c
print('\n\nDone')
