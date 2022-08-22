# Chapter 9
from pathlib import Path
import os
#print(str(Path('spam', 'bacon', 'eggs')))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(Path(r'C:\Users\HP\Desktop\py_folder\book2',filename))

print(Path.cwd())
os.chdir('C:\\Users\\HP\\Desktop\\py_folder')
print(Path.cwd())

print(Path.home())

# os.makedirs() create new folders.
# os.makedirs('C:\\Users\\HP\\Desktop\\py_folder\\book2\\chap9\\os')
# Path(r'C:\\Users\\HP\\Desktop\\py_folder\book2\chap9').mkdir() can create only one folder!!

# os.path.abspath(path) return a absoulute path
print(os.path.abspath('.'))
print(os.path.abspath('.\\book2'))

# anchor is the root
p = Path('C:\\Users\\HP\\Desktop\\py_folder\\book2\\cha7.py')
print(p.anchor)
# parent is the folder which content the current folder
print(p.parent)
# name is the folder name, stem is the name without sub name, suffix is the subname
print(p.name)
print(p.stem)
print(p.suffix)
print(p.drive)

print(os.path.basename(p))
print(os.path.dirname(p))
print(str(os.path.split(p)))
pStr = 'C:\\Users\\HP\\Desktop\\py_folder\\book2\\cha7.py'
print(str(pStr.split(os.sep)))
print(str(os.path.getsize(pStr)))
print(str(os.listdir('C:\\Users\\HP\\Desktop\\py_folder\\book2')))
# glob()
p = Path('C:\\Users\\HP\\Desktop\\py_folder\\book2')
wrongPath = Path('C:\\Users\\HP\\Desktop\\py_folder\\book2\\chapter7.py')
p.glob('*')
print(str(list(p.glob('*'))))
print(str(list(p.glob('*.bat'))))
print(str(list(p.glob('cha?.py'))))
print(str(p.exists()))
print(str(wrongPath.exists()))
print(str(p.is_file()))
print('-----------------------------')
print(Path.cwd())
print(Path.cwd().parents[0])
print(Path.cwd().parents[1])

