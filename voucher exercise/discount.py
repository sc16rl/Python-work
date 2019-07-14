import random
import string

l = 'abcdefghijklmnopqrstuvwxyz'
array = list(l +l.upper())

def shuffle():
    global array
    random.shuffle(array)
    return ''.join(array[:8])

for i in range(200):
    print(shuffle())