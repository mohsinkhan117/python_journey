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
from collections import deque
dq = deque([10, 20, 30])

# Add elements to the right
dq.append(40)  

# Add elements to the left
dq.appendleft(5)  

# extend(iterable)
dq.extend([50, 60, 70]) 
print("After extend([50, 60, 70]):", dq)

# extendleft(iterable)
dq.extendleft([0, 5])  
print("After extendleft([0, 5]):", dq)

# remove method
dq.remove(20)
print("After remove(20):", dq)

# Remove elements from the right
dq.pop()

# Remove elements from the left
dq.popleft()  
print("After pop and popleft:", dq)

# clear() - Removes all elements from the deque
dq.clear()  # deque: []
print("After clear():", dq)




dq =deque([1, 2, 3, 3, 4, 2, 4])

# Accessing elements by index
print(dq[0])  
print(dq[-1]) 

# Finding the length of the deque
print(len(dq))

# 1. Counting occurrences of a value
print(dq.count(20))  # Occurrences of 20
print(dq.count(30))  # Occurrences of 30

# 2. Rotating the deque
dq.rotate(2)  # Rotate the deque 2 steps to the right
print(dq)

dq.rotate(-3)  # Rotate the deque 3 steps to the left
print(dq)

# 3. Reversing the deque
dq.reverse()  # Reverse the deque
print(dq)