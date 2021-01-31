#This code will sort words alphabetically
sentence = input('Enter a sentence: ')
words = sentence.split()
words.sort()
print("The sorted words are: ")
for i in range(len(words)):
    print(str(i+1) + ".", words[i])
