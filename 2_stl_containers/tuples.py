'''
A tuple is an immutable ordered collection of elements.

Tuples are similar to lists, but unlike lists, they cannot be changed after their creation.
Can hold elements of different data types.
These are ordered, heterogeneous and immutable.
'''
tup=('Apple',1,'Mango')
print(tup)


# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)


#can store any type of data structure
tup = (5, 'Welcome', 7.5, True, [1, 2, 3], {'key': 'value'})
print(tup)


#accessing tuple 
tup = tuple("Geeks")
print(tup[0])
print(tup[1:4])  
print(tup[:3])

# Tuple unpacking
tup = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)


t = (1, 2, 3, 4, 5) 
# Reverse the tuple using slicing with a step of -1
rev = t[::-1]

print(rev)


t = (1, 2, 3, 4, 5)  
# Reverse the tuple using the built-in reversed() function and convert it back to a tuple
rev = tuple(reversed(t))
print(rev)