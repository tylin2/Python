# Chapter 4
import random

myPets = ['Zophie', 'Pooka', 'Fat-tail', 'Simon']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named '  + name)
else:
    print(name + ' is my pet.')
print('--------------------------')

'''
enumerate()
'''
print('enumerate(): ')
for i , name in enumerate(myPets):
    print('Index ' + str(i) + ' in names is: ' + name)
print('--------------------------')

'''
random
'''
print('random.choice()')
print(random.choice(myPets))
print('random.shuffle()')
random.shuffle(myPets)
print('After random.shuffle(): ' , end = '')
print(myPets)
print('--------------------------')

'''
index()
'''
print('index()')
print(myPets.index('Zophie'))
print('--------------------------')

'''
append(), insert(), remove(), sort() & resverse()
'''
print('append()')
myPets.append('Footfoot')
print('After myPets.append("Footfoot"): ', end = '')
print(myPets)
print('insert()')
myPets.insert(2, 'Fido')
print('After myPets.insert(2, "Fido"): ', end = '')
print(myPets)
print('remove()')
myPets.remove('Fido')
print('After myPets.remove("Fido"): ', end = '')
print(myPets)
print('sort()')
myPets.sort()
print('After myPets.sort(): ', end = '')
print(myPets)
myPets.sort(reverse = True)
print('After myPets.sort(resverse = True): ', end = '')
print(myPets)
# When the list has int and string, sort() would not be use.
print('reverse()')
myPets.reverse()
print('After myPets.reverse(): ', end = '')
print(myPets)
print('--------------------------')

'''
del
'''
print('del')
del myPets[1]
print('After "del myPets[1]": ', end = '')
print(myPets)
print('--------------------------')

'''
-1
'''
print('List[-?]')
print('Print "myPets[-1]": ', end = '')
print(myPets[-1])
print('Print "myPets[-3]": ', end = '')
print(myPets[-3])
print('--------------------------')

'''
Slice
'''
print('Slice(:) in List')
print('Print "myPets[:]": ', end = '')
print(myPets[:])
print('Print "myPets[1:3]": ', end = '')
print(myPets[1:3])
print('Print "myPets[:2]": ', end = '')
print(myPets[:2])
print('Print "myPets[2:]": ', end = '')
print(myPets[2:])
print('Print "myPets[0:-2]": ', end = '')
print(myPets[0:-2])
print('Slice(:) in String')
catName = 'Zophie a cat'
print('Print "catName": ' + catName)
print('Print "catName[7]": ' + catName[7])
print('Set a new name by "newName = name[0:7] + "the" + name[8:12]"')
newName = name[0:7] + 'the' + name[8:12]
print('Print "newName": ' + newName)
# string can NOT be change by slice, so " catName[7] = 'the' " will get ERROR!!
# catName[7] = 'the'
print('--------------------------')

'''
Tuple
'''
print('Tuple "()"')
print('Set "eggs = ("hello", 42, 0.5)"')
eggs = ("hello", 42, 0.5)
print('Print "type(eggs)": ' + str(type(eggs)))
print('Print "eggs[0]": ' + eggs[0])
print('Print "eggs[1]": ', end = '')
print(eggs[1])
# Tuple can NOT be change value after setting, "eggs[0] = 'hi'" will get ERROR!!!
# eggs[0] = 'hi'
print('--------------------------')

'''
Function to change between list() and tuple()
'''
print('Function to change between list() and tuple()')
print('Print "tuple(["cat", "dog", 5])": ', end = '')
print(tuple(['cat', 'dog', 5]))
print('Print "list(("cat", "dog", 5))": ', end = '')
print(list(('cat', 'dog', 5)))
print('Print "list("hello")": ', end = '')
print(list("hello"))
print('--------------------------')

'''
Reference
'''
print("Reference")
spam = 42
cheese = spam
print('Set spam = 42 and cheese = spam, Print cheese = ' + str(cheese))
spam = 100
print('Then set spam = 100, Print spam = ' + str(spam) + ', cheese = ' + str(cheese))
cheese = 102
print('Then set cheese = 102, Print spam = ' + str(spam) + ', cheese = ' + str(cheese))
spamList = [0, 1, 2, 3, 4, 5]
cheeseList = spamList # The reference is being copied, not the list
print('Set spamList = [0, 1, 2, 3, 4, 5] and cheeceList = spamList, Print cheeseList = ' +
        str(cheeseList))
spamList[2] = 100
print('Then set spamList[2] = 100, Print cheeseList = ' + str(cheeseList))
cheeseList[4] = 102
print('Then set cheeseList[4] = 102, Print spamList = ' + str(spamList) +
        ', cheeseList = ' + str(cheeseList))
print('--------------------------')

'''
id()
'''
print("id()")
print('Print id("Howdy"): ' + str(id('Howdy')))
bacon = 'Hello'
print('Print id(bacon): ' + str(id(bacon)))
bacon += ' world!'
print('Print id(bacon): ' + str(id(bacon)))
print('Print id(myPets): ' + str(id(myPets)))
myPets.append('Miss Cleo')
print('After "myPets.append()", print id(myPets): ' + str(id(myPets)))
