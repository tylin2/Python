# Chapter 6
while True:
    print('Enter you age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
while True:
    print('Select a new password (letters and number only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters an numbers.')
