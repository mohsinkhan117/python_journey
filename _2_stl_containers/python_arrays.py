'''
(A) NumPy arrays
Strictly homogeneous
Enforced at the C level

Example:
np.array([1, 2, 3.5])  # → all converted to float

(B) array (import array as arr)
Also homogeneous
But uses type codes (like 'i', 'f', etc.)


'b'	signed char
'B'	unsigned char
'h'	signed short
'H'	unsigned short
'i'	signed int
'I'	unsigned int
'l'	signed long
'L'	unsigned long
'q'	signed long long
'Q'	unsigned long long
'f'	float
'd'	double
'''



import array as arr

# create integer array using type code 'i'
a = arr.array('i', [1, 2, 3])

# access first element
print(a[0])

# append element to array
a.append(5)
print(a)

# iterate and print elements
for i in range(0, 3):
    print(a[i], end=" ")

print()  # newline for formatting

# insert element at specific index
a.insert(1, 4)
print(*a)

# remove first occurrence of value 1
a.remove(1)
print(a)

# remove element at index 2
a.pop(2)
print(a)

# create Python list
a = [1,2,3,4,5,6,7,8,9,10]

# convert list to array
b = arr.array('i', a)

# slice array from index 3 to 7
res = b[3:8]
print(res)

# slice array from index 5 to end
res = b[5:]
print(res)

# slice entire array
res = b[:]
print(res)

# update element at index 2 in list
a[2] = 6
print(a)

# update element at index 4 in list
a[4] = 8
print(a)

# count occurrences of value 2
count = a.count(2)
print(count)

# reverse list elements
a.reverse()
print(*a)

# extend list with new elements
a.extend([6,7,8,9,10])
print(a)