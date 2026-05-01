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


lst = [1, 2, 2, 3, 3]
unique = list(set(lst))   #used in real world removing duplicates

text = "this is is a test test"
words = set(text.split())
print(words)


# Adding element to the set
s.add("d")
print(s)


a = {1, 2}
b = {1, 2, 3, 4}

print(a.issubset(b))    # True
print(b.issuperset(a))  # True

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
print(a.symmetric_difference(b))  # {1, 2, 4, 5}
a.difference_update(b)
print(a)  # {1}

#short hand methods

print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference
print(a ^ b)  # symmetric difference

if set(a) & set(b):
    print("Common elements exist")

#clear() function removes all elements from a set, leaving it empty.
s = {1, 2, 3}
s.clear()
print(s)



s.remove(2)     # removes 2
# s.remove(5)   # ❌ ERROR if not found

s.discard(5)    # ✅ no error


a = {1, 2}
b = {3, 4}
a.update(b)
print(a)   # {1, 2, 3, 4}


fs = frozenset([1, 2, 3])
# fs.add(4) ❌ ERROR (immutable)


