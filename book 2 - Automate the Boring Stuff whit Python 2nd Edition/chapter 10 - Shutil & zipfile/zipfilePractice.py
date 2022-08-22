# Chapter 10
import zipfile, os
from pathlib import Path

p = Path.cwd()
exampleZip = zipfile.ZipFile(p/'example.zip')
print(exampleZip.namelist())
'''
# getinfo(): to get size and compress_size
spamInfo = exampleZip.getinfo('spam.txt')
print(spamInfo.file_size)
print(spamInfo.compress_size)
print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')
'''
'''
# extractall(): to extract all files
exampleZip.extractall()
'''
'''
# extract(file, folder)
exampleZip.extract('spam.txt')
exampleZip.extract('spam.txt', 'chap10\\cats')
'''
exampleZip.close()

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type = zipfile.ZIP_DEFLATED)
newZip.close()

