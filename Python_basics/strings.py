# ===========================================================
#           PYTHON STRING METHODS - COMPLETE REVISION
# ===========================================================

import re

print("\n================= STRING CREATION =================")
s = "Hello World"
print(s)

s1 = 'Single Quotes'
s2 = "Double Quotes"
s3 = """Triple
Line
String"""

print(s1)
print(s2)
print(s3)

# -----------------------------------------------------------

print("\n================= INDEXING =================")

text = "Python"

print(text[0])      # P
print(text[1])      # y
print(text[-1])     # n
print(text[-2])     # o

# -----------------------------------------------------------

print("\n================= SLICING =================")

print(text[0:3])      # Pyt
print(text[2:6])      # thon
print(text[:4])       # Pyth
print(text[2:])       # thon
print(text[:])        # Python

print(text[::2])      # Pto
print(text[1::2])     # yhn

print(text[::-1])     # Reverse

# -----------------------------------------------------------

print("\n================= STRING LENGTH =================")

print(len(text))

# -----------------------------------------------------------

print("\n================= CONCATENATION =================")

a = "Hello"
b = "World"

print(a + " " + b)

# -----------------------------------------------------------

print("\n================= REPETITION =================")

print("Hi " * 3)

# -----------------------------------------------------------

print("\n================= MEMBERSHIP =================")

print("Py" in text)
print("Java" in text)

print("Java" not in text)

# -----------------------------------------------------------

print("\n================= COMPARISON =================")

print("abc" == "abc")
print("abc" != "ABC")
print("abc" < "xyz")

# -----------------------------------------------------------

print("\n================= CASE METHODS =================")

s = "Hello Python"

print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())
print(s.casefold())

# -----------------------------------------------------------

print("\n================= STRIP METHODS =================")

s = "    Hello Python    "

print(s.strip())
print(s.lstrip())
print(s.rstrip())

# -----------------------------------------------------------

print("\n================= FIND METHODS =================")

s = "Python Programming"

print(s.find("Pro"))
print(s.find("Java"))

print(s.rfind("m"))

# -----------------------------------------------------------

print("\n================= INDEX METHODS =================")

print(s.index("Program"))

# print(s.index("Java"))   # Error

# -----------------------------------------------------------

print("\n================= COUNT =================")

print(s.count("m"))
print(s.count("Python"))

# -----------------------------------------------------------

print("\n================= STARTSWITH / ENDSWITH =================")

print(s.startswith("Python"))
print(s.endswith("ing"))

# -----------------------------------------------------------

print("\n================= REPLACE =================")

print(s.replace("Python", "Java"))

# -----------------------------------------------------------

print("\n================= SPLIT =================")

sentence = "Apple,Banana,Mango"

fruits = sentence.split(",")

print(fruits)

# -----------------------------------------------------------

print("\n================= JOIN =================")

words = ["I", "Love", "Python"]

print(" ".join(words))
print("-".join(words))

# -----------------------------------------------------------

print("\n================= PARTITION =================")

email = "abc@gmail.com"

print(email.partition("@"))

# -----------------------------------------------------------

print("\n================= CENTER / LJUST / RJUST =================")

print("Python".center(20, "-"))
print("Python".ljust(20, "*"))
print("Python".rjust(20, "*"))

# -----------------------------------------------------------

print("\n================= ZFILL =================")

print("25".zfill(5))

# -----------------------------------------------------------

print("\n================= CHECK METHODS =================")

print("abc".isalpha())
print("123".isdigit())
print("abc123".isalnum())
print("Hello".istitle())
print("HELLO".isupper())
print("hello".islower())
print("    ".isspace())

# -----------------------------------------------------------

print("\n================= STRING FORMATTING =================")

name = "Mohsin"
age = 22
cgpa = 3.61

# Old Style (%)

print("Name: %s Age: %d CGPA: %.2f" % (name, age, cgpa))

# format()

print("Name: {} Age: {}".format(name, age))

print("Name: {0} Age: {1}".format(name, age))

# f-string

print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cgpa:.2f}")

# -----------------------------------------------------------

print("\n================= RAW STRING (r'') =================")

path = r"C:\Users\Mohsin\Desktop\Test"

print(path)

# -----------------------------------------------------------

print("\n================= ESCAPE CHARACTERS =================")

print("Hello\nWorld")
print("Hello\tPython")
print("She said \"Hello\"")
print('It\'s Python')

# -----------------------------------------------------------

print("\n================= STRING INTERPOLATION =================")

language = "Python"

print(f"I love {language}")

# -----------------------------------------------------------

print("\n================= STRING ITERATION =================")

for ch in "Python":
    print(ch, end=" ")

print()

# -----------------------------------------------------------

print("\n================= ENUMERATE =================")

for index, value in enumerate("Python"):
    print(index, value)

# -----------------------------------------------------------

print("\n================= ASCII VALUES =================")

print(ord('A'))
print(chr(65))

# -----------------------------------------------------------

print("\n================= MIN / MAX =================")

print(min("Python"))
print(max("Python"))

# -----------------------------------------------------------

print("\n================= SORT CHARACTERS =================")

print(sorted("python"))

# -----------------------------------------------------------

print("\n================= REVERSE STRING =================")

text = "Python"

print(text[::-1])

# -----------------------------------------------------------

print("\n================= REGULAR EXPRESSIONS =================")

sentence = "Python 3.12 was released in 2024."

# Find all numbers

print(re.findall(r"\d+", sentence))

# Find first match

print(re.search(r"released", sentence))

# Replace

print(re.sub(r"\d+", "XXXX", sentence))

# Split

print(re.split(r"\s+", sentence))

# -----------------------------------------------------------

print("\n================= STRING TO LIST =================")

text = "Python"

print(list(text))

# -----------------------------------------------------------

print("\n================= LIST TO STRING =================")

letters = ['P', 'y', 't', 'h', 'o', 'n']

print("".join(letters))

# -----------------------------------------------------------

print("\n================= STRING COMPARISON =================")

a = "apple"
b = "banana"

print(a < b)
print(a > b)

# -----------------------------------------------------------

print("\n================= IMMUTABILITY =================")

s = "Python"

# s[0] = 'J'      # Error

s = "J" + s[1:]

print(s)

# -----------------------------------------------------------

print("\n================= STRING MULTILINE =================")

msg = """
Hello
Welcome
to
Python
"""

print(msg)

s1 = "The BodyGuard is the best album"



# Define the pattern to search for

pattern = r"Body"


# -----------------------------------------------------------
# Use the search() function to search for the pattern in the string

result = re.search(pattern, s1)



# Check if a match was found

if result:

    print("Match found!")

else:

    print("Match not found.")