


# Method 1: Using curly braces {}
student1 = {
    "name": "Jake",
    "age": 22,
    "course": "Computer Science",
    "grades": [85, 90, 88]
}
print("Method 1 ({}):", student1)

# Method 2: Using dict() constructor
student2 = dict(name="Kat", age=20, course="Mathematics")
print("Method 2 (dict()):", student2)

# Method 3: Creating empty dictionary
empty_dict = {}
print("Empty dictionary:", empty_dict)

# ============================================
# 2. ACCESSING DICTIONARY ITEMS
# ============================================

student = {"name": "John", "age": 25, "grade": "A", "city": "New York"}

# Using square brackets [] - raises KeyError if key missing
print(f"Using ['name']: {student['name']}")
print(f"Using ['age']: {student['age']}")

# Using get() method - safe, returns None if key missing
print(f"Using get('grade'): {student.get('grade')}")
print(f"Using get('salary'): {student.get('salary')}")  # Returns None
print(f"Using get('salary', 'Not Found'): {student.get('salary', 'Not Found')}")

# 3. ADDING AND UPDATING ITEMS

inventory = {"apple": 10, "banana": 5, "orange": 8}
print("Original inventory:", inventory)

# Adding new key-value pair
inventory["grape"] = 15
print("After adding 'grape':", inventory)

# Updating existing value
inventory["apple"] = 25
print("After updating 'apple':", inventory)

# Update multiple items using update() method
inventory.update({"mango": 12, "banana": 20})
print("After update() method:", inventory)

# 4. REMOVING DICTIONARY ITEMS

# Create a fresh dictionary for demonstration
data = {1: 'Python', 2: 'Java', 3: 'C++', 4: 'JavaScript', 'language': 'coding'}
print("Original data:", data)

# Method 1: del statement
del data[4]
print("\n1. After del data[4]:", data)

# Method 2: pop() - removes and returns value
removed_value = data.pop(2)
print(f"2. After pop(2) - Removed value: '{removed_value}'")
print(f"   Remaining data: {data}")

# Method 3: popitem() - removes and returns last inserted item
key, value = data.popitem()
print(f"3. After popitem() - Removed: '{key}: {value}'")
print(f"   Remaining data: {data}")

# Method 4: clear() - removes all items
data.clear()
print("4. After clear():", data)

# 5. ITERATING THROUGH DICTIONARIES

courses = {
    101: "Python Programming",
    102: "Data Structures",
    103: "Web Development",
    104: "Machine Learning"
}
print("Dictionary:", courses)
print()

# Iterate over keys only
print("Iterating over KEYS only:")
for key in courses:
    print(f"  Key: {key}")

# Using keys() method
print("\n Using keys() method:")
for key in courses.keys():
    print(f"  Course ID: {key}")

# Iterate over values only
print("\n Using values() method:")
for value in courses.values():
    print(f"  Course Name: {value}")

# Iterate over key-value pairs
print("\n Using items() method:")
for key, value in courses.items():
    print(f"  ID {key} -> {value}")

# 6. NESTED DICTIONARIES

# Creating a nested dictionary
university = {
    "Computer Science": {
        "courses": ["Python", "Java", "SQL"],
        "students": 120,
        "professors": ["Dr. Smith", "Dr. Jones"]
    },
    "Mathematics": {
        "courses": ["Calculus", "Algebra", "Statistics"],
        "students": 95,
        "professors": ["Dr. Brown", "Dr. Davis"]
    },
    "Physics": {
        "courses": ["Mechanics", "Thermodynamics", "Quantum"],
        "students": 80,
        "professors": ["Dr. Wilson"]
    }
}

print("Nested dictionary structure:")
for dept, details in university.items():
    print(f"\n Department: {dept}")
    for key, value in details.items():
        print(f"   {key}: {value}")

# Accessing nested dictionary values
print("\n Accessing nested values:")
print(f"CS courses: {university['Computer Science']['courses']}")
print(f"Math professors: {university['Mathematics']['professors'][0]}")

# 7. ADDITIONAL USEFUL DICTIONARY METHODS

sample = {"a": 1, "b": 2, "c": 3, "d": 4}
print("Sample dictionary:", sample)

# len() - get number of items
print(f"1. Length (len()): {len(sample)} items")

# in operator - check if key exists
print(f"2. 'a' in sample: {'a' in sample}")
print(f"   'z' in sample: {'z' in sample}")

# copy() - create a shallow copy
sample_copy = sample.copy()
print(f"3. Copy (copy()): {sample_copy}")

# fromkeys() - create dict from sequence
keys = ['x', 'y', 'z']
new_dict = dict.fromkeys(keys, 0)
print(f"4. fromkeys() with default 0: {new_dict}")

# setdefault() - get value or set if key doesn't exist
value1 = sample.setdefault('e', 5)
value2 = sample.setdefault('a', 99)
print(f"5. setdefault('e', 5): returns {value1}, now dict: {sample}")
print(f"   setdefault('a', 99): returns {value2} (unchanged)")

# 8. PRACTICAL EXAMPLES

# Example 1: Student Grade Book
print("📊 EXAMPLE 1: Student Grade Book")
grade_book = {
    "Alice": {"Math": 85, "English": 90, "Science": 88},
    "Bob": {"Math": 78, "English": 82, "Science": 79},
    "Charlie": {"Math": 92, "English": 88, "Science": 94}
}

for student, grades in grade_book.items():
    average = sum(grades.values()) / len(grades)
    print(f"{student}: Average = {average:.1f}")

# Example 2: Word Counter
print("\n📝 EXAMPLE 2: Word Frequency Counter")
text = "the cat and the dog and the bird"
word_freq = {}
for word in text.split():
    word_freq[word] = word_freq.get(word, 0) + 1
print(f"Text: '{text}'")
print(f"Word frequency: {word_freq}")

# Example 3: Dictionary Comprehension
print("\n🔄 EXAMPLE 3: Dictionary Comprehension")
squares = {x: x**2 for x in range(1, 6)}
cubes = {x: x**3 for x in range(1, 6)}
print(f"Squares: {squares}")
print(f"Cubes: {cubes}")

# Example 4: Merging dictionaries (Python 3.9+)
print("\n🔗 EXAMPLE 4: Merging Dictionaries")
dict1 = {"name": "John", "age": 30}
dict2 = {"city": "Boston", "job": "Engineer"}
merged = {**dict1, **dict2}  # Using unpacking
print(f"dict1: {dict1}")
print(f"dict2: {dict2}")
print(f"Merged: {merged}")

# 9. ERROR HANDLING WITH DICTIONARIES

config = {"host": "localhost", "port": 8080}

# Safe access using get()
port = config.get("port", 80)
timeout = config.get("timeout", 30)  # Default value 30

print(f"Config: {config}")
print(f"Port (using get): {port}")
print(f"Timeout (using get with default): {timeout}")

# Handling KeyError with try-except
try:
    missing = config["database"]
except KeyError as e:
    print(f"KeyError caught: Key {e} does not exist!")

print("\n✅ Dictionary operations completed successfully!")