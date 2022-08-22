# Chapter 7
import re
while True:
    print('Enter a date(DD/MM/YYYY): ')
    user = input()
    if user == '':
        break

    dateRegex = re.compile(r'(\d{2})\/(\d{2})\/(\d{4})')
    userInput  = dateRegex.search(user)
    if userInput == None:
        print('Please enter the date follow the format')
        continue
    dd, mm, yy = dateRegex.search(user).groups()
    if int(yy) < 1000 or int(yy) > 2999 or int(mm) > 12 or int(mm) < 1 or int(dd) < 1 or int(dd) > 31:
        print('Please enter the date between 1000/01/01 and 2999/12/31')
        continue
    if int(mm) == 2:
        if int(yy) % 4 == 0 and int(dd) > 29:
            print('Please enter the correct date for Feb')
            continue
        else:
            if int(dd) > 28:
                print('Please enter the correct date for Feb, theis year is not a leap year.')
                continue
    elif (int(mm) > 7 and int(mm) % 2 == 0) or (int(mm) <= 7 and int(mm) % 2 == 1):
        if int(dd) > 31:
            print('Please enter the correct date for long month')
            continue
    elif (int(mm) > 7 and int(mm) % 2 == 1) or (int(mm) <= 7 and int(mm) % 2 == 0):
        if int(dd) > 30:
            print('Please enter the correct date for short month')
            continue
print('Done')


