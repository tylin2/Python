# Chapter 5
import pprint

massege = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for ch in massege:
    count.setdefault(ch,0)
    count[ch] = count[ch] + 1

print(count)
pprint.pprint(count)
print(pprint.pformat(count))
