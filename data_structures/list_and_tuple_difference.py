import copy

# ============================================================
# LIST vs TUPLE METHODS — SIDE-BY-SIDE REVISION SHEET
# Lists are MUTABLE  (can change after creation)
# Tuples are IMMUTABLE (cannot change after creation)
# That single difference explains why lists have MANY methods
# and tuples have only TWO.
# ============================================================

# ------------------------------------------------------------
# QUICK COMPARISON TABLE (read this first)
# ------------------------------------------------------------
#   LIST METHOD          TUPLE METHOD        _NOTE
#   --------------------  ------------------  ------------------------------
#   append()              --                  no tuple equivalent (can't grow)
#   extend()               --                  no tuple equivalent
#   insert()               --                  no tuple equivalent
#   remove()                --                  no tuple equivalent
#   pop()                   --                  no tuple equivalent
#   clear()                 --                  no tuple equivalent
#   sort()                  --                  no tuple equivalent (can't reorder in place)
#   reverse()               --                  no tuple equivalent (in-place)
#   copy()                  --                  tuples don't need copy() (immutable = safe to reuse)
#   count()                 count()             SAME on both -> counts occurrences
#   index()                  index()             SAME on both -> finds position
# ------------------------------------------------------------
# Only count() and index() exist on BOTH, because they only
# READ data -> they don't need to modify the list/tuple.
# Everything else is list-only, since it changes the object.
# ------------------------------------------------------------


print("\n================= CREATION =================")
my_list = [10, 20, 30, 40, 50]     # square brackets -> mutable
my_tuple = (10, 20, 30, 40, 50)    # round brackets -> immutable

print(my_list)
print(my_tuple)

# -----------------------------------------------------------

print("\n================= INDEXING & SLICING (SAME FOR BOTH) =================")
# Indexing/slicing works identically on lists and tuples -
# this part doesn't depend on mutability.
print(my_list[0], my_tuple[0])       # first item
print(my_list[-1], my_tuple[-1])     # last item
print(my_list[1:3], my_tuple[1:3])   # slice

# -----------------------------------------------------------

print("\n================= LENGTH / MEMBERSHIP / LOOPING (SAME FOR BOTH) =================")
print(len(my_list), len(my_tuple))          # length works the same
print(20 in my_list, 20 in my_tuple)        # membership check works the same
for item in my_tuple:                        # looping works the same
    pass

# -----------------------------------------------------------

print("\n================= COUNT() — AVAILABLE ON BOTH =================")
# count(value) -> how many times a value appears
nums_list = [1, 2, 2, 3, 2]
nums_tuple = (1, 2, 2, 3, 2)

print(nums_list.count(2))    # list version
print(nums_tuple.count(2))   # tuple version -> works exactly the same way

# -----------------------------------------------------------

print("\n================= INDEX() — AVAILABLE ON BOTH =================")
# index(value) -> position of first occurrence, raises ValueError if missing
print(nums_list.index(2))    # list version -> 1
print(nums_tuple.index(2))   # tuple version -> 1 (identical behavior)

# -----------------------------------------------------------

print("\n================= APPEND() — LIST ONLY =================")
# append(value) -> adds a single item to the end (in place)
my_list.append(60)
print(my_list)

# my_tuple.append(60)   # AttributeError: tuples have no append()
# Reason: appending changes the object's size -> not allowed on immutables

# -----------------------------------------------------------

print("\n================= EXTEND() — LIST ONLY =================")
# extend(iterable) -> adds multiple items from another list/iterable
my_list.extend([70, 80])
print(my_list)

# my_tuple.extend((70, 80))   # AttributeError: no extend() on tuples
# Workaround for tuples: create a NEW tuple by concatenation instead
my_tuple = my_tuple + (70, 80)   # this doesn't modify, it builds a new tuple
print(my_tuple)

# -----------------------------------------------------------

print("\n================= INSERT() — LIST ONLY =================")
# insert(index, value) -> adds an item at a specific position
my_list.insert(0, 5)
print(my_list)

# my_tuple.insert(0, 5)   # AttributeError: no insert() on tuples
# Workaround: slice + concatenate to build a new tuple
my_tuple = (5,) + my_tuple
print(my_tuple)

# -----------------------------------------------------------

print("\n================= REMOVE() — LIST ONLY =================")
# remove(value) -> deletes the FIRST matching value
my_list.remove(5)
print(my_list)

# my_tuple.remove(5)   # AttributeError: no remove() on tuples
# Workaround: convert to list, remove, convert back
temp = list(my_tuple)
temp.remove(5)
my_tuple = tuple(temp)
print(my_tuple)

# -----------------------------------------------------------

print("\n================= POP() — LIST ONLY =================")
# pop(index) -> removes AND returns an item (default: last item)
popped = my_list.pop()
print(popped, my_list)

# my_tuple.pop()   # AttributeError: no pop() on tuples
# Workaround: slicing to simulate a "pop"
last_item = my_tuple[-1]
my_tuple = my_tuple[:-1]
print(last_item, my_tuple)

# -----------------------------------------------------------

print("\n================= CLEAR() — LIST ONLY =================")
# clear() -> empties the list completely, in place
temp_list = [1, 2, 3]
temp_list.clear()
print(temp_list)

# temp_tuple.clear()   # AttributeError: no clear() on tuples
# Workaround: just reassign to an empty tuple
temp_tuple = (1, 2, 3)
temp_tuple = ()
print(temp_tuple)

# -----------------------------------------------------------

print("\n================= SORT() — LIST ONLY =================")
# sort() -> reorders the list in place (ascending by default)
unsorted_list = [3, 1, 4, 1, 5]
unsorted_list.sort()
print(unsorted_list)

unsorted_list.sort(reverse=True)   # descending order
print(unsorted_list)

# unsorted_tuple.sort()   # AttributeError: no sort() on tuples
# Workaround: sorted() returns a NEW LIST (not a tuple) -> wrap in tuple()
unsorted_tuple = (3, 1, 4, 1, 5)
sorted_tuple = tuple(sorted(unsorted_tuple))
print(sorted_tuple)

# -----------------------------------------------------------

print("\n================= REVERSE() — LIST ONLY =================")
# reverse() -> reverses the list in place
rev_list = [1, 2, 3]
rev_list.reverse()
print(rev_list)

# rev_tuple.reverse()   # AttributeError: no reverse() on tuples
# Workaround: slicing with step -1 (works on both, but doesn't modify in place)
rev_tuple = (1, 2, 3)
rev_tuple = rev_tuple[::-1]
print(rev_tuple)

# -----------------------------------------------------------

print("\n================= COPY() — LIST ONLY (concept differs for tuples) =================")
# copy() -> shallow copy of a list, useful to avoid shared-reference bugs
list_a = [1, 2, 3]
list_b = list_a.copy()
list_b.append(4)
print(list_a, list_b)   # list_a unaffected -> proves it's a separate copy

# Tuples don't offer/need copy(): since they're immutable, you can safely
# reuse the SAME tuple everywhere without any risk of it changing.
tuple_a = (1, 2, 3)
tuple_b = tuple_a         # just assign directly, no copy needed
print(tuple_a, tuple_b)

# -----------------------------------------------------------

print("\n================= WHY THE DIFFERENCE EXISTS =================")
# Lists   -> designed for data that changes over time (grow/shrink/reorder)
# Tuples  -> designed for fixed data (coordinates, records, dict keys)
#            Because tuples never change, Python can:
#              - use them as dictionary keys / set elements (lists can't)
#              - make them slightly faster & more memory-efficient
print("Tuple as dict key:", {(1, 2): "point A"})
# print({[1, 2]: "point A"})   # TypeError: list is unhashable, can't be a dict key


# ============================================================
# ============================================================
# LIST ALIASING vs CLONING — QUICK REVISION SHEET
# Aliasing -> two variable names point to the SAME list in memory
# Cloning  -> a NEW, separate list is created (independent copy)
# ============================================================


print("\n================= ALIASING =================")
# Aliasing happens when you assign a list to another variable
# using plain '=' . No new list is created - both names refer
# to the exact same object in memory.
list_a = [1, 2, 3]
list_b = list_a          # list_b is just another name for list_a (alias)

print(list_a)
print(list_b)

print(id(list_a))        # same memory address...
print(id(list_b))        # ...as this one
print(list_a is list_b)  # True -> confirms they are the SAME object

# -----------------------------------------------------------

print("\n================= WHY ALIASING IS DANGEROUS =================")
# Since both names point to the same object, changing one
# changes the other too - this often causes accidental bugs.
list_b.append(4)

print(list_a)   # [1, 2, 3, 4] -> changed even though we only touched list_b!
print(list_b)   # [1, 2, 3, 4]

# -----------------------------------------------------------

print("\n================= CLONING (SHALLOW COPY METHODS) =================")
# Cloning creates a NEW list object with the same values,
# so changes to the clone do NOT affect the original.

original = [1, 2, 3]

# Method 1: slicing [:]
clone1 = original[:]

# Method 2: list() constructor
clone2 = list(original)

# Method 3: .copy() method
clone3 = original.copy()

# Method 4: list comprehension (less common, but works)
clone4 = [item for item in original]

print(original is clone1)   # False -> different objects, confirms real clone
print(original is clone2)   # False
print(original is clone3)   # False
print(original is clone4)   # False

print(original == clone1)   # True -> same VALUES, just not same OBJECT

# Prove independence: modifying a clone leaves the original untouched
clone1.append(99)
print(original)   # [1, 2, 3]        -> unaffected
print(clone1)      # [1, 2, 3, 99]   -> only the clone changed

# -----------------------------------------------------------

print("\n================= SHALLOW COPY LIMITATION (NESTED LISTS) =================")
# IMPORTANT: all 4 methods above are SHALLOW copies.
# A shallow copy duplicates the OUTER list, but inner/nested
# lists inside it are still shared (aliased), not cloned.
nested = [[1, 2], [3, 4]]
shallow = nested.copy()          # or nested[:] or list(nested)

shallow.append([5, 6])           # adding a new outer item -> safe, doesn't affect original
print(nested)     # [[1, 2], [3, 4]]              -> original unaffected here
print(shallow)    # [[1, 2], [3, 4], [5, 6]]

shallow[0].append(99)            # modifying an INNER list -> this leaks through!
print(nested)     # [[1, 2, 99], [3, 4]]   -> original changed too! (shared inner list)
print(shallow)    # [[1, 2, 99], [3, 4], [5, 6]]

# -----------------------------------------------------------

print("\n================= DEEP COPY (TRUE FULL CLONE) =================")
# deepcopy() -> recursively clones EVERYTHING, including nested
# lists/dicts, so there is NO sharing at any level.
nested2 = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested2)

deep[0].append(100)               # modify an inner list on the deep copy
print(nested2)    # [[1, 2], [3, 4]]        -> completely unaffected
print(deep)       # [[1, 2, 100], [3, 4]]   -> only the deep copy changed

# -----------------------------------------------------------

print("\n================= QUICK COMPARISON =================")
#   TECHNIQUE              RESULT                          SAFE FOR NESTED LISTS?
#   ---------------------  ------------------------------  ------------------------
#   list_b = list_a         ALIAS (same object)              No -> not a copy at all
#   original[:]             shallow clone (new outer list)   No -> inner lists still shared
#   list(original)           shallow clone                    No -> inner lists still shared
#   original.copy()          shallow clone                    No -> inner lists still shared
#   copy.deepcopy(original)  full independent clone            Yes -> fully separate at every level