# Chapter 9
from pathlib import Path

print(Path.cwd())
print(Path.home())
'''
# create a file called spam.txt and write 'Hello, world!' in that, then read and print it
p = Path('spam.txt')
p.write_text('Hello, world!')
print(p.read_text())
'''

'''
helloFile = open(Path.cwd()/'hello.txt')
helloContent = helloFile.read()
print(helloContent)

sonnetFile = open('sonnet29.txt')
print(sonnetFile.readlines())
'''

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()

baconFile = open('bacon.txt','a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)


