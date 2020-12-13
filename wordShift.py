#code
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
word = input('Enter a word: ')
shiftValue = int(input('Enter a shift value: '))
newWord = ""

for i in range(0,len(word)):
    for j in range(0,len(alphabets)):
        #condition
        if word[i] == alphabets[j]:
            if j+shiftValue > 26:
                newWord = newWord + alphabets[j+shiftValue%26]
            else:
                newWord = newWord + alphabets[j+shiftValue]
print("New word : "+newWord)
