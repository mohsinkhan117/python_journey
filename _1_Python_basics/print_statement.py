# 1. Basic printing - multiple items
print("Hello", "World", "Python")  # Output: Hello World Python

# 2. Default separator (space) vs custom separator
print("Apple", "Banana", "Cherry")  # Default: space between
print("Apple", "Banana", "Cherry", sep="-")  # Custom: Apple-Banana-Cherry
print("Apple", "Banana", "Cherry", sep="")   # No separator: AppleBananaCherry
print("Apple", "Banana", "Cherry", sep="\n") # New line between each

# 3. End parameter - what to print at the end (default is \n)
print("Hello", end=" ")  # Ends with space instead of newline
print("World", end="!!!")  # Ends with !!!
print("Python")  # Output: Hello World!!!Python

# 4. Printing to file instead of console
with open("output.txt", "w") as file:
    print("This goes to file", file=file)

# 5. Flush parameter - force output immediately (useful for loading bars)
import time
print("Loading", end="", flush=True)
for i in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)  # Shows dots one by one

# 6. Print variables
name = "Alice"
age = 25
print(name, age)  # Simple: Alice 25

# 7. String concatenation
print("Name: " + name + ", Age: " + str(age))  # Manual: Name: Alice, Age: 25

# 8. Multiple arguments (auto converts to string)
print("Value:", 100, "is", True)  # Output: Value: 100 is True


grade = 85

# f-string (f"...") - EVALUATES the {expression}
print(f"Grade: {grade}")  
# Output: Grade: 85
# Python calculates {grade} → replaces with actual value

# Regular string - TREATS {grade} as literal text
print("Grade: {grade}")  
# Output: Grade: {grade}
# Python sees it as plain text, doesn't calculate anything

# To understand the difference:
x = 10
y = 20

print(f"Sum: {x + y}")     # Output: Sum: 30 (calculates)
print("Sum: {x + y}")      # Output: Sum: {x + y} (literal text)

name = "Alice"
print(f"Upper: {name.upper()}")  # Output: Upper: ALICE (executes method)
print("Upper: {name.upper()}")   # Output: Upper: {name.upper()} (just text)