# Chapter 6
print('Escape character(\)')
# \\ can make \ to be shown.
print("Print Bob\\'s mother: " + 'Bob\'s mother')
# Put 'r' before '' or "" means this is a raw string, it can use for showing a URL.
print(r"C:\Users\HP\Desktop\py_folder\book2")
print('------------------------------------------------')
#'''
print('''Dear Alice,

Eve's cat hasbeen arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
print('------------------------------------------------')
#Slice
spam = 'Hello world!'
print("sapm[0]: " + spam[0])
print("sapm[-1]: " + spam[-1])
print("sapm[0:5]: " + spam[0:5])
print("sapm[:5]: " + spam[:5])
print("sapm[6:]: " + spam[6:])
fizz = spam[:5]
print("fizz: " + fizz)
print('------------------------------------------------')
# in and not in
print('"Hello" in "Hello World": ' + str("Hello" in "Hello World"))
print('"HELLO" not in "Hello World": ' + str("HELLO" not in "Hello World"))
print('"" in "spam": ' + str("" in "spam"))
print('------------------------------------------------')
# % and f
name = 'Al'
age = 4000
print(r'Using %: ' + 'My name is %s. I am %s years old.'%(name, age))
print(f'Using f: My name is {name}. Next year I will be {age + 1}.')
print('------------------------------------------------')
# upper(), lower(), isupper(), isslower()
upperSpam = spam.upper()
print(f'upperSpam: {upperSpam}')
lowerSpam = spam.lower()
print(f'lowerSpam: {lowerSpam}')
print('spam.islower(): ' + str(spam.islower()))
print('"HELLO".isupper(): ' + str("HELLO".isupper()))
print('"12345".isupper() | "12345".islower(): '
        + str("12345".isupper()) + ' | ' + str("12345".islower()))
print('------------------------------------------------')
# isX()
print('"hello".isalpha(): ' + str("hello".isalpha()))
print('"hello123".isalpha(): ' + str("hello123".isalpha()))
print('"123".isdecimal(): ' + str("123".isdecimal()))
print('"    ".isspace(): ' + str("    ".isspace()))
print('"".isspace(): ' + str("".isspace()))
print('"Hello World!".istitle(): ' + str("Hello World!".istitle()))
print('"Hello World 123!".istitle(): ' + str("Hello World 123!".istitle()))
print('"Hello world!".istitle(): ' + str("Hello world!".istitle()))
print('"Hello WOrld!".istitle(): ' + str("Hello WOrld!".istitle()))
# isalnum() is to check the string have numbers or alphas.
print('"hello".isalnum(): ' + str("hello".isalnum()))
print('"123!".isalnum(): ' + str("123!".isalnum()))
print('"".isalnum(): ' + str("".isalnum()))
print('"    ".isalnum(): ' + str("  ".isalnum()))
print('------------------------------------------------')
# join() and split()
print("', '.join(['cats', 'rats', 'bats']) :" + str(', '.join(['cats', 'rats', 'bats'])))
print("' '.join(['My', 'name', 'is', 'Simon']) :" + str(' '.join(['My', 'name', 'is', 'Simon'])))
print("'ABC'.join(['My', 'name', 'is', 'Simon']) :" + str('ABC'.join(['My', 'name', 'is', 'Simon'])))
print("'My name is Simon'.split(): " + str('My name is Simon'.split()))
print("'My name is Simon'.split('m'): " + str('My name is Simon'.split('m')))
letter = '''Dear Alice,
How have you been?I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Bob'''
print(r"letter.split('\n'): " + str(letter.split('\n')))
print('------------------------------------------------')
# partition()
print("'Hello, world!'.partition('w'): " + str('Hello, world!'.partition('w')))
print("'Hello, world!'.partition('world'): " + str('Hello, world!'.partition('world')))
print("'Hello, world!'.partition('o'): " + str('Hello, world!'.partition('o')))
print("'Hello, world!'.partition('ZYX'): " + str('Hello, world!'.partition('XYZ')))
before, sep, after = 'Hello, world!'.partition(' ')
print('before | after | sep. : ' + f'{before} | {after} | {sep}.')
print('------------------------------------------------')
# rjust(), ljust(), center()
print("'Hello'.rjust(20): " + 'Hello'.rjust(20))
print("'Hello'.ljust(20,'*'): " + 'Hello'.ljust(20, '*'))
print("'Hello'.center(20,'+'): " + 'Hello'.center(20, '+'))
print('------------------------------------------------')
# strip(), rstrip(), lstrip()
spaceSpam = '   Hello World    '
print("spaceSpam.strip(): " + spaceSpam.strip())
print("spaceSpam.lstrip(): " + spaceSpam.lstrip())
print("spaceSpam.rstrip(): " + spaceSpam.rstrip())
longSpam = 'SpamSpamBaconSpamEggsSpamSpam'
print('longSpam.strip("ampS"): ' + longSpam.strip('ampS'))
print('------------------------------------------------')
# ord(), chr()
print("ord('A'): " + str(ord('A')))
print("chr(65): " + chr(65))
print('------------------------------------------------')
# pyperclip
'''
# Can be use in Shell
import pyperclip
pyperclip.copy('Hello World...')
print(pyperclip.paste())
'''
