#This code will calculate number of vowels in a given word
word = input("Enter string: ")
vowels=0
for i in word:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels = vowels + 1
print("Number of vowels are: " + str(vowels))
