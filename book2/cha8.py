# Chapter 8
'''
1.
    No, we need to install.
2.
    make program shorter.
3.
    Int: user only enter the integer
    float : user can enter float
4.
    pyip.inputInt(min = 0, max = 99)
5.
    r'' is not allow, will be refuse
6.
    error(RetryLimitException)
7.
    hello
'''
import pyinputplus as pyip
totalPrice = 0
breadMenu = {'wheat':1.5, 'white':1.75, 'sourdough':2}
proteinMenu = {'chicken':7, 'turkey':9, 'ham':8.5,'tofu':5.99}
cheeseMenu = {'no':0, 'cheddar':1,'Swiss':1.5, 'mozzarella':1.5}
mayoMenu = {'no':0, 'yes':0.5}
mustardMenu = {'no':0, 'yes':0.5}
lettuceMenu = {'no':0, 'yes':0.5}
tomatoMenu = {'no':0, 'yes':0.5}

while True:
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='Please select one of the bread: \n')
    totalPrice += breadMenu[bread]
    protein = pyip.inputMenu(['chicken', 'turkey', 'ham','tofu'], prompt='Please select one of the protein: \n')
    totalPrice += proteinMenu[protein]
    cheese = pyip.inputYesNo('Enter Yes or No for adding cheeses: ')
    if cheese == 'yes':
        cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt='Please select one of the cheese: \n')
    totalPrice += cheeseMenu[cheese]
    mayo = pyip.inputYesNo('Enter Yes or No for adding mayo: ')
    totalPrice += mayoMenu[mayo]
    mustard = pyip.inputYesNo('Enter Yes or No for adding mustard: ')
    totalPrice += mustardMenu[mustard]
    lettuce = pyip.inputYesNo('Enter Yes or No for adding lettuce: ')
    totalPrice += lettuceMenu[lettuce]
    tomato = pyip.inputYesNo('Enter Yes or No for adding tomato: ')
    totalPrice += tomatoMenu[tomato]
    many = pyip.inputInt('Enter how many sandwitchs you want: ', min = 1)
    totalPrice *= many
    nextSand = pyip.inputYesNo('Enter Yes or No for adding another Sandwich: ')
    if nextSand == 'Yes':
        continue
    else:
        break
print('TotalPrice: ' + str(totalPrice))
