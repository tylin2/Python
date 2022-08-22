# Chapter 6
'''
1.
    \
2.
    \n: new line
    \t: a tab
3.
    \\
4.
    Because ' is in the ""
5.
    """
6.
    'e', 'Hello',''Hello', 'lo world!'
7.
    'HELLO', True, 'hello'
8.
    ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
    'There-can-be-only-one.'
9.
    rjust(), ljust(), center()
10.
    ljust(), rjust()
'''

def printTable(data):
    for x in range(len(data[0])):
        for y in range(len(data)):
            print(data[y][x].rjust(10), end = ' ')
        print('')

tableData = [['Apple', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

