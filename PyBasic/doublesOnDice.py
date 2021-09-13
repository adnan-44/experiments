# Program to count total numbers of trials to get same numbers on 2 dices
import random
count = 1   # number of 

# Method to roll dices
def roll():
    global count
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print("\nDice 1: ",d1)
    print("Dice 2: ",d2)
    if d1 != d2:
        roll()
        count += 1

print("Rolling dice....")
roll()
print("\nTotal trials to get doubles:", count)