import random, sys
print('ROCK, PAPER, SCISSORS')

w = 0 #wins
l = 0 #losses
t = 0 #ties

while True:
    print(str(w) + ' Wins, ' + str(l) + ' Losses, ' + str(t) + ' Ties')
    print('Enter you move: (r)ock (p)aper (s)cissors or (q)uit')
    u = input() # user input
    ui = 0
    if u == 'p':
        print('PAPER versus...')
        ui = 3
    elif u == 'r':
        print('ROCK versus...')
        ui = 1
    elif u == 's':
        print('SCISSORS versus...')
        ui = 2
    elif u == 'q':
        sys.exit()
    else:
        print('Error input! Type one of r, p, s, or q.')
        continue
    c = random.randint(1,3)

    if c == 1:
        print('ROCK')
    elif c == 2:
        print('SCISSORS')
    elif c == 3:
        print('PAPER')

    if c == ui:
        print('It is a tie!')
        t = t + 1
    elif (ui == 1 and c == 2) or (ui == 2 and c == 3) or (ui == 3 and c == 1):
        print('You win!')
        w = w + 1
    elif (ui == 1 and c == 3) or (ui == 2 and c == 1) or (ui == 3 and c == 2):
        print('You lose!')
        l = l + 1
