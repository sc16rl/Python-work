import random
import string

l = 'abcdefghijklmnopqrstuvwxyz'
array = list(l +l.upper())

def shuffle():
    global array
    random.shuffle(array)
    x = ''.join(array[:8])
    return x

new_list = []
i=0
while i < 200:
    if shuffle() in new_list:
        continue
    else:
        new_list.append(shuffle())
        i+=1

for j in new_list:
    print(j)
