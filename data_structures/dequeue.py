'''
A deque stands for Double-Ended Queue. It is a special type of data structure that 
allows to add and remove elements from both ends efficiently. This makes it useful 
in applications like task scheduling, sliding window problems and real-time data processing.
'''

#collections generally means data structures used to store and manage groups of data.
# Examples:

# list
# tuple
# set
# dict

# These are built-in collections.

# But Python also provides a specialized module called
# 👉 collections

# This module contains advanced collection data types that extend or improve basic ones.

from collections import deque 
de = deque(['name','age','DOB']) 
print(de)



'''
Why Do We Need deque?
It supports O(1) time for adding/removing elements from both ends.
It is more efficient than lists for front-end operations.
It can function as both a queue (FIFO) and a stack (LIFO).
Ideal for scheduling, sliding window problems and real-time data processing.
It offers powerful built-in methods like appendleft(), popleft() and rotate().
Types of Restricted Deque
Input Restricted Deque:  Input is limited at one end while deletion is permitted at both ends.
Output Restricted Deque: output is limited at one end but insertion is permitted at both ends.
Appending and Deleting Deque Items
append(x): Adds x to the right end of the deque.
appendleft(x): Adds x to the left end of the deque.
extend(iterable): Adds all elements from the iterable to the right end.
extendleft(iterable): Adds all elements to the left end, but elements are inserted one by one from the iterable, resulting in a reversed order.
remove(value): Removes the first occurrence of the specified value from the deque. If value is not found, it raises a ValueError.
pop(): Removes and returns an element from the right end.
popleft(): Removes and returns an element from the left end.
clear(): Removes all elements from the deque.
'''