# Chapter 5

birthdayArr1 = ['Alice', 'Bob', 'Carol']
birthdayArr2 = ['Bob', 'Alice', 'Carol']

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4', 'Lisa': 'Aug 5'}
birthdays2 = {'Carol': 'Mar 4', 'Lisa': 'Aus 5', 'Bob': 'Dec 12', 'Alice': 'Apr 1'}

print('Print birthdays["Alice"] : ' + birthdays['Alice'])
print('Pring birthdayArr1 == birthdayArr2: ', end ='')
print(birthdayArr1 == birthdayArr2)
print('Print if birthdays == birthdays2: ', end = '')
print(birthdays == birthdays2)

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their dirthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

print('---------------')
print('Print for v in birthdays.values(): ', end = '')
for v in birthdays.values():
    print(v, end = ', ')
print('')
print('---------------')
print('Print for k in birthdays.keys(): ', end = '')
for k in birthdays.keys():
    print(k, end = ', ')
print('')
print('---------------')
print('Print for i in birthdays.items(): ')
for i in birthdays.items():
    print(i)
print('---------------')
print('list(birthdays.keys()): ', end = '')
print(list(birthdays.keys()))
print('---------------')
print('Print for k, v in birthdays.items(): ')
for k, v in birthdays.items():
    print('k: ' + k + ', v: ' + v)
print('')
print('---------------')
print('Print "Alice" in birthdays.keys(): ', end ='')
print('Alice' in birthdays.keys())
print('Print "Mar 4" in birthdays.values(): ', end ='')
print('Mar 4' in birthdays.values())
print('Print "Name" in birthdays.keys(): ', end ='')
print('Name' in birthdays.keys())
print('Print "Name" not in birthdays.keys(): ', end ='')
print('Name' not in birthdays.keys())
print('---------------')
print('birthdays.get(key, if Null return value)')
print("Print Alice's birthday is " + birthdays.get('Alice', 'N/A') + '.')
print("Print Simon's birthday is " + birthdays.get('Simon', 'N/A') + '.')
print('---------------')
print('birthdays.setdefault(key,value)')
birthdays.setdefault('Sally', 'Aug 18')
print('After birthdays.setdefault("Sally", "Aug 18"):')
print(birthdays)
birthdays.setdefault('Lisa', 'Oct 8')
print('After birthdays.setdefault("Lisa", "Oct 8"):')
print(birthdays)
# if key is in the dict, the value will NOT be changed.
