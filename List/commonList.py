#code to find common elements in two lists
l1 = [12,45,23,34,54,98,45]
l2 = [66,98,90,75,23,87]
for i in l1:
   for j in l2:
      if i == j:
         print(i,' is common')
