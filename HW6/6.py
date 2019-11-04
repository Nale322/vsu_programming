import math
import random

storage = [[] for x in range(20)]
a = random.randint(0, 100)

def hash(key):
    index = math.sqrt(a)
    return int(index)

def set_value(key, value):
    index = hash(key)
    for i in storage[index]:
        if key == i[0]:
            i[1] = value
            break    
    else:    
        storage[index].append([key, value])

def get_value(key):
    index = hash(key)
    for i in storage[index]:
        if key == i[0]:
            return i[1]


def del_value(key):
    index = hash(key)
    for i in storage[index]:
        if key == i[0]:
            storage[index].remove(i)
            break


set_value('abc', 1)
set_value('abc', 2)

set_value('cba', 4)
set_value('cba', 10)

set_value('XYN', 3)
set_value('XYN', 31)
print(storage)
del_value('XYN')

print(get_value('abc'))
print(get_value('cba'))
print(get_value('XYN'))

print(storage)
