# Chapter 11
'''
1.
    assert spam >= 10, 'The spam var is less than 10.'
2.
    assert eggs.upper() != bacon.upper(), 'The eggs and bacon var are the same.'
3.
    assert False, 'This assertion always triggers.'
4.
    import logging
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
5.
    import logging
    logging.basicConfig(filename='programLog.txt',level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
6.
    debug, info, warning, error,critial
7.
    logging.disable(logging.CRITIAL)
8.
    print() needs to delete line by line, logging only needs to add the disable().
9.
    step in: get into next function.
    step out: go over the function which we are in now.
    steo over: go over the next function.
10.
    Meeting breakpoints or the end of program will be stopped.
11.
    Click the area before the code line.
'''
