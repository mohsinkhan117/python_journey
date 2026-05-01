fruits = ['apple', 'banana','Mango']
integers=[1,2,3,5,6,8]
mixed =[1,'Apple', 'Mango']
print(fruits)
print (integers)
print(mixed)

#Using list() Constructor: A list can also be created by passing an iterable (such as tuple, string or another list) to the list() constructor.
a = list((1, 2, 3, 'apple', 4.5))  
print(a)

b = list("GFG")
print(b)

# Creating List with Repeated Elements: A list with repeated elements can be created using the multiplication (*) operator.
a=[2]*5
b=[7]*7

print(a)
print(b)



'''
Internal Representation of Lists
Python list stores references to objects, not the actual values directly.

The list keeps memory addresses of objects like integers, strings, or booleans.
Actual objects exist separately in memory.
Modifying a mutable object inside a list changes the original object.
Reassigning an immutable object creates a new object instead of changing the old one.
'''

a = [10, 20, "GfG", 40, True]
print(a)        
print(a[0])     
print(a[1])  
print(a[2])


a = [10, 20, 30, 40, 50]
print(a[0])    
print(a[-1]) #will access last element of the list 
print(a[-2])# 2nd last
print(a[-3])# 3rd last
print(a[1:4])   # elements from index 1 to 3


'''
Adding Elements into List
Elements can be added to a list using the following methods:

append(): Adds an element at the end of the list.
extend(): Adds multiple elements to the end of the list.
insert(): Adds an element at a specific position.
clear(): removes all items.
'''

a = []

a.append(10)  
print("After append(10):", a)  

a.insert(0, 5)
print("After insert(0, 5):", a) 

a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 

a.clear()
print("After clear():", a)

'''
Removing Elements from List
Elements can be removed from a list using the following methods:

remove(): Removes the first occurrence of an element.
pop(): Removes the element at a specific index or the last element if no index is specified.
del statement: Deletes an element at a specified index.
'''

a = [10, 20, 30, 40, 50]

a.remove(30)  
print("After remove(30):", a)

popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

del a[0]  
print("After del a[0]:", a)


'''
Nested lists
'''

matrix =[[1,2,3],
         [4,5,6],
         [7.8,9]]
print(matrix) #complete list
print(matrix[1][2]) #specifix index
