# Chapter 4
'''
1.
    Null list
2.
    spam[2] = 'hello'
3.
    d
4.
    d
5.
    [a, b]
6.
    1
7.
    [3.14, 'cat', 11, 'cat', True, 99]
8.
    [3.14, 11, 'cat', True]
9.
    +, *
10.
    append("something") = add something to end
    insert(place, "something") = assign a place to add something
11.
    del, reomve()
12.
    we can get value by [].
13.
    list is displied by [], but tuple is displied by ().
    list can be edited by list[?], but tuple can not.
14.
    (42,)
15.
    list(tuple), tuple(list)
16.
    id
17.
    deepcopy() is used for copy the list there has list in that.
'''
'''
spam = ['apple', 'bananas', 'tofu', 'cats']
def addComma(someList):
        ans = ''
        for i in range(len(someList)):
            ans += someList[i]
            if i == len(someList) - 2:
                ans += ', and '
            elif i != len(someList) - 1:
                ans += ', '
        return ans
newSpam = addComma(spam)
print(newSpam)
spam = []
newSpam = addComma(spam)
print(newSpam)
'''
'''
import random
numberOfStreak = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    ranString = ''
    for i in range(100):
        ranString += random.choice(['H', 'T'])
    # Code that checks if there is a streak of 6 heads or tails in a rows.
    for i in range(94):
        if i == 94:
            if ranString[i:] == 'HHHHHH' or ranString[i:] == 'TTTTTT':
                numberOfStreak += 1
        else:
            if ranString[i:i+6] == 'HHHHHH' or ranString[i:i+6] == 'TTTTTT':
                numberOfStreak += 1
print('Chance of streak: %s%%' % (numberOfStreak / 10000))
'''
grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]
for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end = '')
    print('')
