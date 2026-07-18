import re

# ============================================================
# STRINGS IN PYTHON — QUICK REVISION SHEET
# Grouped by topic, with short comments on every method.
# ============================================================

print("\n================= STRING CREATION =================")
# Strings can be created with single, double, or triple quotes.
s = "Hello World"
print(s)

s1 = 'Single Quotes'          # single quotes
s2 = "Double Quotes"          # double quotes
s3 = """Triple
Line
String"""                     # triple quotes -> allows multi-line strings

print(s1)
print(s2)
print(s3)

# -----------------------------------------------------------

print("\n================= INDEXING =================")
# Indexing: access a single character. Positive index from left (0),
# negative index from right (-1).
text = "Python"

print(text[0])      # P   -> first char
print(text[1])      # y   -> second char
print(text[-1])     # n   -> last char
print(text[-2])     # o   -> second last char

# -----------------------------------------------------------

print("\n================= SLICING =================")
# Slicing: text[start:stop:step] -> extract a substring.
print(text[0:3])      # Pyt   -> chars from index 0 to 2
print(text[2:6])      # thon  -> chars from index 2 to 5
print(text[:4])       # Pyth  -> from start to index 3
print(text[2:])       # thon  -> from index 2 to end
print(text[:])        # Python -> full copy of string

print(text[::2])      # Pto   -> every 2nd char
print(text[1::2])     # yhn   -> every 2nd char starting at index 1

print(text[::-1])     # Reverse the string (step = -1)

# -----------------------------------------------------------

print("\n================= STRING LENGTH =================")
# len() -> number of characters in the string
print(len(text))

# -----------------------------------------------------------

print("\n================= CONCATENATION =================")
# + joins two strings together
a = "Hello"
b = "World"

print(a + " " + b)

# -----------------------------------------------------------

print("\n================= REPETITION =================")
# * repeats a string n times
print("Hi " * 3)

# -----------------------------------------------------------

print("\n================= MEMBERSHIP =================")
# in / not in -> check if a substring exists inside a string
print("Py" in text)
print("Java" in text)

print("Java" not in text)

# -----------------------------------------------------------

print("\n================= COMPARISON =================")
# Strings compared lexicographically (dictionary order, by ASCII values)
print("abc" == "abc")
print("abc" != "ABC")
print("abc" < "xyz")

# -----------------------------------------------------------

print("\n================= CASE METHODS =================")
# Methods that change letter case
s = "Hello Python"

print(s.upper())       # ALL UPPERCASE
print(s.lower())       # all lowercase
print(s.title())       # Title Case Each Word
print(s.capitalize())  # Capitalize only first letter
print(s.swapcase())    # swap upper<->lower
print(s.casefold())    # aggressive lowercase (for case-insensitive comparisons)

# -----------------------------------------------------------

print("\n================= STRIP METHODS =================")
# Remove unwanted leading/trailing whitespace (or given chars)
s = "    Hello Python    "

print(s.strip())     # removes both sides
print(s.lstrip())    # removes left side only
print(s.rstrip())    # removes right side only

# -----------------------------------------------------------

print("\n================= FIND METHODS =================")
# find() -> returns index of first match, or -1 if not found (no error)
s = "Python Programming"

print(s.find("Pro"))     # found -> returns starting index
print(s.find("Java"))    # not found -> -1

print(s.rfind("m"))      # find() but searches from the right

# -----------------------------------------------------------

print("\n================= INDEX METHODS =================")
# index() -> same as find(), but raises ValueError if not found
print(s.index("Program"))

# print(s.index("Java"))   # Error -> raises ValueError

# -----------------------------------------------------------

print("\n================= COUNT =================")
# count() -> number of non-overlapping occurrences of a substring
print(s.count("m"))
print(s.count("Python"))

# -----------------------------------------------------------

print("\n================= STARTSWITH / ENDSWITH =================")
# Check the beginning / ending of a string
print(s.startswith("Python"))
print(s.endswith("ing"))

# -----------------------------------------------------------

print("\n================= REPLACE =================")
# replace(old, new) -> returns a new string with replacements
print(s.replace("Python", "Java"))

# -----------------------------------------------------------

print("\n================= SPLIT =================")
# split(sep) -> breaks a string into a list based on separator
sentence = "Apple,Banana,Mango"

fruits = sentence.split(",")

print(fruits)

# -----------------------------------------------------------

print("\n================= JOIN =================")
# join() -> opposite of split(); combines list items into one string
words = ["I", "Love", "Python"]

print(" ".join(words))
print("-".join(words))

# -----------------------------------------------------------

print("\n================= PARTITION =================")
# partition(sep) -> splits into 3 parts: (before, sep, after)
email = "abc@gmail.com"

print(email.partition("@"))

# -----------------------------------------------------------

print("\n================= CENTER / LJUST / RJUST =================")
# Padding/alignment methods -> (width, fill_char)
print("Python".center(20, "-"))   # centered
print("Python".ljust(20, "*"))    # left-aligned, padded on right
print("Python".rjust(20, "*"))    # right-aligned, padded on left

# -----------------------------------------------------------

print("\n================= ZFILL =================")
# zfill(width) -> pads string with leading zeros (useful for numbers)
print("25".zfill(5))

# -----------------------------------------------------------

print("\n================= CHECK METHODS =================")
# is...() methods -> return True/False, useful for validation
print("abc".isalpha())     # only letters?
print("123".isdigit())     # only digits?
print("abc123".isalnum())  # only letters/digits?
print("Hello".istitle())   # is title case?
print("HELLO".isupper())   # all uppercase?
print("hello".islower())   # all lowercase?
print("    ".isspace())    # only whitespace?

# -----------------------------------------------------------

print("\n================= STRING FORMATTING =================")
# Three ways to format strings: % operator, .format(), f-strings (best/modern)
name = "Mohsin"
age = 22
cgpa = 3.61

# Old Style (%)
print("Name: %s Age: %d CGPA: %.2f" % (name, age, cgpa))

# format()
print("Name: {} Age: {}".format(name, age))

print("Name: {0} Age: {1}".format(name, age))   # positional args

# f-string (recommended, Python 3.6+)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"CGPA: {cgpa:.2f}")   # :.2f -> 2 decimal places

# -----------------------------------------------------------

print("\n================= RAW STRING (r'') =================")
# r"" -> treats backslashes as literal characters (no escaping)
path = r"C:\Users\Mohsin\Desktop\Test"

print(path)

# -----------------------------------------------------------

print("\n================= ESCAPE CHARACTERS =================")
# \n newline, \t tab, \" escaped quote, \' escaped apostrophe
print("Hello\nWorld")
print("Hello\tPython")
print("She said \"Hello\"")
print('It\'s Python')

# -----------------------------------------------------------

print("\n================= STRING INTERPOLATION =================")
# f-string lets you embed variables directly inside a string
language = "Python"

print(f"I love {language}")

# -----------------------------------------------------------

print("\n================= STRING ITERATION =================")
# Strings are iterable -> loop through each character
for ch in "Python":
    print(ch, end=" ")

print()

# -----------------------------------------------------------

print("\n================= ENUMERATE =================")
# enumerate() -> gives (index, character) pairs while looping
for index, value in enumerate("Python"):
    print(index, value)

# -----------------------------------------------------------

print("\n================= ASCII VALUES =================")
# ord() -> char to ASCII/Unicode number, chr() -> number to char
print(ord('A'))
print(chr(65))

# -----------------------------------------------------------

print("\n================= MIN / MAX =================")
# min()/max() -> smallest/largest character based on ASCII value
print(min("Python"))
print(max("Python"))

# -----------------------------------------------------------

print("\n================= SORT CHARACTERS =================")
# sorted() -> returns a sorted LIST of characters (not a string)
print(sorted("python"))

# -----------------------------------------------------------

print("\n================= REVERSE STRING =================")
# Common trick: slicing with step -1 reverses a string
text = "Python"

print(text[::-1])

# -----------------------------------------------------------

print("\n================= REGULAR EXPRESSIONS =================")
# Quick intro to regex basics before the deep-dive section below
sentence = "Python 3.12 was released in 2024."

# Find all numbers
print(re.findall(r"\d+", sentence))

# Find first match (returns a Match object)
print(re.search(r"released", sentence))

# Replace matches with new text
print(re.sub(r"\d+", "XXXX", sentence))

# Split string using regex pattern
print(re.split(r"\s+", sentence))

# -----------------------------------------------------------

print("\n================= STRING TO LIST =================")
# list() -> converts string into a list of individual characters
text = "Python"

print(list(text))

# -----------------------------------------------------------

print("\n================= LIST TO STRING =================")
# "".join(list) -> converts list of chars back into a string
letters = ['P', 'y', 't', 'h', 'o', 'n']

print("".join(letters))

# -----------------------------------------------------------

print("\n================= STRING COMPARISON =================")
# Comparison operators work alphabetically (ASCII-based)
a = "apple"
b = "banana"

print(a < b)
print(a > b)

# -----------------------------------------------------------

print("\n================= IMMUTABILITY =================")
# Strings CANNOT be modified in place. You must create a new string.
s = "Python"

# s[0] = 'J'      # Error -> TypeError: strings are immutable

s = "J" + s[1:]   # workaround: build a new string

print(s)

# -----------------------------------------------------------

print("\n================= STRING MULTILINE =================")
# Triple-quoted strings preserve line breaks exactly as typed
msg = """
Hello
Welcome
to
Python
"""

print(msg)


# -----------------------------------------------------------
# Simple search example before the detailed regex section
s1 = "The BodyGuard is the best album"

# Define the pattern to search for
pattern = r"Body"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")


# ============================================================
# REGEX (re MODULE) — DETAILED REVISION SECTION
# All core functions grouped together with sample data below.
# ============================================================

text = """
My name is Mohsin.
Email: mohsin@gmail.com
Backup: khan117@yahoo.com
Phone: 03001234567
Office: 091-1234567
CNIC: 17301-1234567-1
Python version 3.13 was released in 2026.
"""

print("=" * 60)
print(text)

# ==========================================================
# 1. search()
# Scans the WHOLE string, returns first Match object or None
# ==========================================================

print("\n1. re.search()")

match = re.search(r"Python", text)

if match:
    print(match.group())   # matched text
    print(match.start())   # start index
    print(match.end())     # end index
    print(match.span())    # (start, end) tuple

# ==========================================================
# 2. match()
# Checks ONLY at the very beginning of the string
# ==========================================================

print("\n2. re.match()")

print(re.match(r"My", text))       # text doesn't start with "My" here (leading \n) -> None
print(re.match(r"Python", text))   # also None, same reason

# ==========================================================
# 3. fullmatch()
# ENTIRE string must match the pattern, start to end
# ==========================================================

print("\n3. re.fullmatch()")

print(re.fullmatch(r"\d+", "12345"))
print(re.fullmatch(r"\d+", "123ABC"))   # fails, extra non-digit chars

# ==========================================================
# 4. findall()
# Returns a LIST of all non-overlapping matches (strings)
# ==========================================================

print("\n4. re.findall()")

print(re.findall(r"\d+", text))

emails = re.findall(r"\S+@\S+", text)   # simple email pattern
print(emails)

# ==========================================================
# 5. finditer()
# Like findall() but returns an ITERATOR of Match objects
# (useful when you need position info for each match)
# ==========================================================

print("\n5. re.finditer()")

for m in re.finditer(r"\d+", text):
    print(m.group(), m.start())

# ==========================================================
# 6. sub()
# Replace all matches with a new string
# ==========================================================

print("\n6. re.sub()")

new_text = re.sub(r"\d+", "XXXX", text)

print(new_text)

# ==========================================================
# 7. subn()
# Same as sub(), but also returns the number of replacements made
# ==========================================================

print("\n7. re.subn()")

result = re.subn(r"\d+", "NUM", text)

print(result)   # (new_string, count)


# 8. split()
# Split a string using a regex pattern (supports multiple delimiters)

print("\n8. re.split()")

sentence = "Apple,Banana;Orange Mango"

print(re.split(r"[,; ]+", sentence))   # split on comma, semicolon, or space


# 9. compile()
# Pre-compile a pattern for reuse -> faster when used many times

print("\n9. re.compile()")

pattern = re.compile(r"\d+")

print(pattern.findall(text))


# 10. escape()
# Escapes special regex characters in a string so it's treated literally

print("\n10. re.escape()")

print(re.escape("www.google.com"))   # dots become \.


# ==========================================================
# COMMON REGEX PATTERN CHEAT SHEET
# \d digit | \w word char | \s whitespace
# \D \W \S -> opposite (non-digit / non-word / non-space)
# + one or more | * zero or more | [A-Z] char range
# ==========================================================

print("\nPATTERN EXAMPLES")

print("Digits:")
print(re.findall(r"\d", text))          # single digits

print("Multiple Digits:")
print(re.findall(r"\d+", text))         # digit groups (numbers)

print("Letters:")
print(re.findall(r"[A-Za-z]+", text))   # words made of letters only

print("Capital Letters:")
print(re.findall(r"[A-Z]", text))       # individual capital letters

print("Small Letters:")
print(re.findall(r"[a-z]", text))       # individual lowercase letters

print("Words:")
print(re.findall(r"\w+", text))         # word characters (letters/digits/_)

print("Non Words:")
print(re.findall(r"\W", text))          # punctuation, spaces, symbols

print("Spaces:")
print(re.findall(r"\s", text))          # whitespace characters

print("Non Spaces:")
print(re.findall(r"\S+", text))         # chunks with no whitespace