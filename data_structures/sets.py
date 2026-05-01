'''
A Set in Python is used to store a collection of items with the following properties.

No duplicate elements. If try to insert the same item again, it overwrites previous one.
An unordered collection. When we access all items, they are accessed without any specific order and we cannot access items using indexes as we do in lists.
Internally use hashing that makes set efficient for search, insert and delete operations. It gives a major advantage over a list for problems with these operations.
Mutable, meaning we can add or remove elements after their creation, the individual elements within the set cannot be changed directly.
'''

s={1,3,4,6,3}
print(s)
print(type(s))

# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding element to the set
s.add("d")
print(s)

#union of set
a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
print(u)

#intersection of set
a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(i)

#difference() function returns a set containing elements that are in the first set but not in the second.
a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d)

#clear() function removes all elements from a set, leaving it empty.
s = {1, 2, 3}
s.clear()
print(s)