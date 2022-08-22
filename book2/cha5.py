# chapter 5
'''
1.
    {}
2.
    {'foo': 42}
3.
    dict stores data without order,
    but list stores data whit order.
4.
    KeyError
5.
    nothing different
6.
    'cat' in spam is to know there is key is 'cat'
    cat in spam.values() is to know there is value is 'cat'
7.
    spam.setdefault('color', 'black')
8.
    pprint.pprint()
'''
'''
chessBoard = {'1h': 'bking', '6c': 'wqueen', '8g': 'bbishop', '5h': 'bqueen', '3e':'wking',
              '2a':'bbishop', '2b':'wbishop'}
def isValidChessBoard(board):
    count = {}
    for k, v in board.items():
        c = int(k[0])
        if c > 8 or c < 1:
            return False
        r = k[1:]
        if r != 'a' and r != 'b' and r != 'c' and r != 'd' and r != 'e' and r != 'f' and r != 'g' and r != 'h' :
            return False
        color = v[0]
        if color != 'w' and color != 'b':
            return False
        count.setdefault(v[0],0)
        count[v[0]] = count[v[0]] + 1
        chess = v[1:]
        if chess != 'pawn' and chess != 'knight' and chess != 'bishop' and chess != 'rook' and chess != 'queen' and chess != 'king':
            return False
        count.setdefault(v,0)
        count[v] = count[v] + 1
    print(count)
    for k, v in count.items():
        if k == 'b' or k == 'w':
            if v > 16:
                return False
        if k == 'bqueen' or k == 'bking' or k == 'wqueen' or k == 'wking':
            if v > 1:
                return False
        if k == 'bknight' or k == 'bbishop' or k == 'brook' or k == 'wknight' or k == 'wbishop' or k == 'wrook':
            if v > 2:
                return False
        if k == 'bpawn' or k == 'wpawn':
            if v > 8:
                return False
    return True

print(isValidChessBoard(chessBoard))
'''

def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        #FILL IN THE CODE HERE
        print(str(v) + " " + k)
        item_total = item_total + v
    print("Total number of item: " + str(item_total))
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(stuff)


def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] = inventory[item] + 1
    return inventory

inv = {'gold coin':42, 'rope':1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'rudy']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
