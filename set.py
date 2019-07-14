from functools import reduce

data = [[1,3,5,6], [2,5,6,9], [5,6,11,15]]

new = [set(i) for i in data]

print(reduce(lambda x,y: x&y, new))

## string

a = ['a','b','c']

print(";".join(a))