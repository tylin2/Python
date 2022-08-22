# Chapter 10
import shutil, os
from pathlib import Path
print(Path.cwd())
p = Path.cwd()
'''
# shutil.copy(file, new file name or copy to the folder name)
shutil.copy(p/'bacon.txt',p/'bacon2.txt')
shutil.copy(p/'bacon.txt',p/'chap9')
'''
'''
# shutil.copytree(folder, copy to)
shutil.copytree(p/'chap10', p/'chap10_backup')
'''
'''
# shutil.move(source, destination with new name)
shutil.move('chap9\\bacon.txt', 'chap10')
shutil.move('chap10\\bacon.txt', 'chap10_backup\\new_bacon.txt')
'''
# os.unlink(path): delete a file with path
# os.rmdir(path): delete a empty folder
# os.tmtree(path): delete a folder which is NOT empty
