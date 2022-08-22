# Chapter 6
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches':4, 'apples':12, 'cups':4, 'cookies':800}
printPicnic(picnicItems,12,4)
printPicnic(picnicItems,20,6)
