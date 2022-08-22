### if
'''
name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo')
else:
    print('You are neither Alice not a little kid.')
'''
'''
elif age > 100:
    print('You are not Alice, grannie')

elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
'''
'''
elif age > 100:
    print('You are not Alice, grannie')
'''


### while
'''
name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')
'''

'''
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is a password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')
'''

name = ''
while not name:
    print('Enter your name: ')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough room for all you guests')
print('Done')
