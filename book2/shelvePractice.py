# Chapter 9
import shelve

shelfFile = shelve.open('mydata')
print(type(shelfFile))
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
#print(shelfFile['cats'])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
