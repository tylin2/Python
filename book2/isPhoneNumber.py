# Chapter 7
import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False  # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # not an area code
    if text[3] != '-':
        return False  # does not have first hyphen
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # does not have first 3 digits
    if text[7] != '-':
        return False  # does not have second hyphen
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # does not have last 4 digits
    return True  # "text" is a phone number!

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

phoneNumRegex1 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex1.search('My number is 415-555-4242.')
print('Phone number found: ' + mo1.group())
'''
findall()
'''
print('phoneNumRegex1.findall(message): ' + str(phoneNumRegex1.findall(message)))

'''
group()
'''
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex2.search('My number is 415-555-4242.')
print('Phone number found: ' + mo2.group())
print('mo2.group(0): ' + mo2.group(0))
print('mo2.group(1): ' + mo2.group(1))
print('mo2.group(2): ' + mo2.group(2))
print('mo2.groups(): ' + str(mo2.groups()))
areaCode, mainNumber = mo2.groups()
print('areaCode: ' + areaCode + ', mainNumber: ' + mainNumber)
print('phoneNumRegex2.findall(message): ' + str(phoneNumRegex2.findall(message)))

phoneNumRegex3 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo3 = phoneNumRegex3.search('My number is (415) 555-4242.')
print('mo3.group(1): ' + mo3.group(1))
print('mo3.group(2): ' + mo3.group(2))


'''
Pipe(|)
'''
heroRegex = re.compile(r'Batman|Tina Fey')
mo4 = heroRegex.search('Batman and Tina Fey.')
print('mo4.group(): ' + mo4.group())
mo5 = heroRegex.search('Tina Fey and Batman.')
print('mo5.group(): ' + mo5.group())
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo6 = batRegex.search('Batmobile lost a wheel')
print('mo6.group(): ' + mo6.group())
print('mo6.group(1): ' + mo6.group(1))
'''
?
'''
batRegex2 = re.compile(r'Bat(wo)?man')
mo7 = batRegex2.search('The Adventure of Batman')
print('mo7.group(): ' + mo7.group())
mo8 = batRegex2.search('The Adventure of Batwoman')
print('mo8.group(): ' + mo8.group())
'''
*: 0 or more than 0 time, ex. Bat(wo)*man => batwowowoman
+: 1 or more than 1 time, ex. Bat(wo)+mon => batwoman, batwowowoman | batman => None
{}: assign the times, ex. (Ha){3} => HaHaHa | (Ha){3,5} => HaHaHa, HaHaHaHa, HaHaHaHaHa |
                          (Ha){3,} => more than 3 times Ha
'''
'''
greedy and non-greedy
'''
greedyHaRegex =re.compile(r'(Ha){3,5}')
mo9 = greedyHaRegex.search('HaHaHaHaHa')
print('mo9.group(): ' + mo9.group())
nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo10 = nonGreedyHaRegex.search('HaHaHaHaHa')
print('mo10.group(): ' + mo10.group())
