# Chapter 9
'''
1.
    the direction which base on now position
2.
    an specific address for a file, all of them start at root
3.
    C:/Users/AL
4.
    Error
5.
    os.getcwd(): get the folder where we are now
    os.chdir(): change the current folder
6.
    .: current folder
    ..: parent folder
7.
    root name: C:\bacon\eggs
    base name: spam.txt
8.
    r, w, a
9.
    delete the original words
10.
    with \n or not
11.
    dict
'''
from pathlib import Path
import re

'''
print('Enter an adjective: ')
adj1 = input()

print('Enter a noun: ')
n1 = input()

print('Enter a verb: ')
v1 = input()

print('Enter a noun: ')
n2 = input()

p = Path('MadLibs.txt')
message = p.read_text().split()
print(message)

for i in range(len(message)):
    if message[i] == 'ADJECTIVE':
        message[i] = adj1
    elif message[i] == 'VERB.':
        message[i] = v1 + '.'
    elif message[i] == 'NOUN':
        if i < 9:
            message[i] = n1
        else:
            message[i] = n2

newFile = open('MadLibsNew.txt', 'w')
newFile.write(' '.join(message))
newFile.close()
'''

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4}){1,2} # dot-something
    )''', re.VERBOSE)

p = Path(r'C:\Users\HP\Desktop\py_folder\book2')
allTxt = list(p.glob('*.txt'))

for txt in allTxt:
    txtFile = open(txt)
    message = txtFile.read()
    for groups in emailRegex.findall(message):
        print(groups[0])

