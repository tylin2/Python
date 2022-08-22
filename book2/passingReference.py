# Chapter 4
import copy

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(str(spam))
print('--------------------------')

'''
copy() and deepcopy()
'''
spam = ['A', 'B', 'C', 'D']
print('id(spam): ' + str(id(spam)))
cheese = copy.copy(spam)
print('id(cheese): ' + str(id(cheese)))
cheese[1] = 42
print('cheese: ' + str(cheese))
print('spam: ' + str(spam))
