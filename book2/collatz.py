# Chaper 3
def collatz(num):
    if(num % 2 == 0):
        return num // 2
    else:
        return 3 * num + 1

try:
    print('Enter number: ')
    n = int(input())
    while(n != 1):
        n = collatz(n)
        print(n)
except ValueError:
    print('Enter a integer number.')
