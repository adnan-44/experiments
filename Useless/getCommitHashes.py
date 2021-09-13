# Basic and Useless program to get hashes from git history and write in 'hashes.txt'
# It requires 'history.txt', to get this file for your repo, simply run " git log --oneline --max-count=25 > history.txt "

import os

file = open('history.txt')
hashes = list()
for line in file:
    parts = line.split()
    hashes.append(parts[0])
file.close()

# write hashes from list to file
file = open('hashes.txt', 'x')
for hash in hashes:
    data = hash + "\n"
    file.write(data)
print('Hashes:', hashes)
