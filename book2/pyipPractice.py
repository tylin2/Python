# Chapter 8
import pyinputplus as pyip

#response = input('Enter a number: ')

# inputStr(), inputNum(), inputChoice(), inputMenu(), inputDatetime(), inputYesNo()
# inputBool(), inputEmail(), inputFilepath(), inputPassword()

# min(>=), max(<=), greaterThan(>), lessThan(<)
# blank = True, accept user to enter space or blank
# limit = 2, allow user to enter twice.
# timeout = 5, ask the answer be entered in 5 sec.
# default = 'N/A', return the value(N/A), if there is a exception
# allowRegexes = [r'(I|V|X|L|C|D|M)+',r'zero'], allow user to anser roman numbers and zero.
# blockRegexes = [r'[02468]$'], set user can not enter a number end with '02468'
response = pyip.inputNum(blockRegexes = [r'[02468]$'])
print('response: ', end='')
print(response)
