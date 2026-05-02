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
'''


import array as arr
a = arr.array('i', [1, 2, 3])

# accessing First Araay
print(a[0])

# adding element to array
a.append(5)
print(a)