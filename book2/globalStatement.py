# Chapter 3
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
print('Before calling spam(): ' + eggs)
spam()
print('After calling spam(): ' + eggs)
