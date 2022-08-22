# Chapter 7
import re
'''
\d: 0~9
\D: Except 0~9
\w: A/a~Z/z, 0~9, _
\W: Except A/a~Z/z, 0~9, _
\s: Space, tab, new Line
\S: Except Space, tab, new Line
'''
stuff = "12 drummers, 11 popers, 10lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"
xmasRegex = re.compile(r'\d+\s*\w+')
print('xmasRegex.findall(stuff): ' + str(xmasRegex.findall(stuff)))

'''
create char by myself
'''
vowelRegex = re.compile(r'[aeiouAEIOU]')
print('vowelRegex.findall(stuff): ' + str(vowelRegex.findall(stuff)))
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print('consonantRegex.findall(stuff): ' + str(consonantRegex.findall(stuff)))

'''
^, $
'''
# '^...' means start with ...
beginsWithHello = re.compile(r'^Hello')
print('beginsWithHello.search("Hello world!"): ' + str(beginsWithHello.search("Hello world!")))
# '...$' means end with ...
endsWithNumber = re.compile(r'\d$')
print('endsWithNumber.search("Your number is 42"): ' + str(endsWithNumber.search("Your number is 42")))

'''
wildcard(.): find words expect new line.
'''
atRegex = re.compile(r'.at')
message = 'The cat in the hate sat at the flat mat.'
print('atRegex.findall(message): ' + str(atRegex.findall(message)))
'''
.*
'''
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo1 = nameRegex.search('First Name: Al Arom  Last Name: Sweigart Something')
print('mo1.group(1): ' + mo1.group(1))
print('mo1.group(2): ' + mo1.group(2))

'''
re.I: Ignore case
'''
robocop = re.compile(r'robocop', re.I)
message = 'Robocop is part man , part machine, all cop.'
print('robocop.search(message).group(): ' + robocop.search(message).group())

'''
sub(): replace words
'''
namesRegex = re.compile(r'Agent \w+')
subNameRegex = namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
print(subNameRegex)
agentNamesRegex = re.compile(r'Agent (\w)\w*')
secretName = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(secretName)
