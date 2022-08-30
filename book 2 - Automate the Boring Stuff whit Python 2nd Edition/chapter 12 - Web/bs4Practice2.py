# Chapter 12
import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')


# select(): #author -> id=author, .notice -> CSS class name = notice,
# div>span -> span in div, there is no other thing between them,
# input[name] or input[type='button']
elems = exampleSoup.select('#author')
print("type(elems), len(elems): " + str(type(elems)) + ', ' + str(len(elems)))
print("type(elems[0]): " + str(type(elems[0])))
print("elems[0]: " + str(elems[0]))
print("elems[0].getText(): " + elems[0].getText())
print("elems[0].attrs: " + str(elems[0].attrs))

pElems = exampleSoup.select('p')
print("pElems[0]: " + str(pElems[0]))
print("pElems[0].getText(): " + pElems[0].getText())
print("pElems[1]: " + str(pElems[1]))
print("pElems[1].getText(): " + pElems[1].getText())
print("pElems[2]: " + str(pElems[2]))
print("pElems[2].getText(): " + pElems[2].getText())

soup = bs4.BeautifulSoup(open('example.html'),'html.parser')
spanElem = soup.select('span')[0]
print("spanElem: " + str(spanElem))
print("spanElem.get('id'): " + spanElem.get('id'))
print(spanElem.get('some_nonexisten_addr') == None)
print(spanElem.attrs)
