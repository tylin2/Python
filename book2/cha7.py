# Chapter 7
'''
1.
    re.compile()
2.
    r can make / not to define
3.
    None or a Match Object
4.
    group()
5.
    [0]: 000-111-1111, [1]: 000, [2]: 111-1111
6.
    (): group \(\), .: except new line \.
7.
    without group: string, with group: a list of string
8.
    pipe, a(a|b) means find aa or ab
9.
    (b)? means without b or repeat b one time.
    ? means nongreedy search, return the shortest answer.
10.
    (b)+ means repeat b one or more than one times.
    (b)* means without b or repeat b more than one times.
11.
    {3}: find word repeat 3 times.
    {3,5}: find word repeat over 3 times and up to 5 times.
12.
    \d: 0~9, \w: a-zA-Z0-9_, \s: space, tab, \n
13.
    \D: expect 0-9, \W: expect \w, \S: Expect \s
14.
    .*: greedy search
    *?: non greedy search
15.
    [0-9a-z]
16.
    re.I
17.
    . is to compare with any other char expect \n, re.DOTALL means . will compare with \n
18.
    X drummers, X pipers, five rings, X hens
19.
   re.VERBOSE:  the string is added space
20.
    r'^\d{1,3}(,\d{3})*$'
21.
    r'[A-Z][a-z]*\sWatanabe'
22.
    r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.'
'''
