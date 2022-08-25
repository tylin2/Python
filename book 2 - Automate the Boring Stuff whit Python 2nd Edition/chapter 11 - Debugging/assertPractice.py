# Chapter 11
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print(ages)
assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.

# AssertionError
ages.reverse()
print(ages)
assert ages[0] <= ages[-1] # Assert that the first age is <= the last age.
