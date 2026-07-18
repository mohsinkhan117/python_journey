

fileName = r"D:\Python_journey\_5_files\Example1.txt"

# ==========================================================
#           PYTHON FILE WRITING - QUICK REVISION
# ==========================================================

fileName = r"D:\Python_journey\_5_files\Output.txt"

# ==========================================================
# Open file in Write Mode
# ==========================================================

# Creates a new file if it doesn't exist.
# If the file already exists, everything inside is erased.

with open(fileName, "w") as file:

    file.write("Hello Python")

# ==========================================================
# Write Multiple Lines
# ==========================================================

with open(fileName, "w") as file:

    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

# ==========================================================
# Write a List of Strings
# ==========================================================

fruits = [
    "Apple\n",
    "Banana\n",
    "Orange\n"
]

with open(fileName, "w") as file:

    file.writelines(fruits)



# ==========================================================
# Copy one file into another
# ==========================================================

source = r"D:\Python_journey\_5_files\Example1.txt"
destination = r"D:\Python_journey\_5_files\Example2.txt"

with open(source, "r") as src:

    data = src.read()

with open(destination, "w") as dst:

    dst.write(data)

# ==========================================================
# Copy file line by line
# ==========================================================

source = r"D:\Python_journey\_5_files\Example1.txt"
destination = r"D:\Python_journey\_5_files\Example3.txt"

with open(source, "r") as src, open(destination, "w") as dst:

    for line in src:

        dst.write(line)



# ==========================================================
# Append to a File
# ==========================================================

# Keeps existing data and adds new content at the end.

with open(fileName, "a") as file:

    file.write("\nNew line added.")

# ==========================================================
# Append Multiple Lines
# ==========================================================

with open(fileName, "a") as file:

    file.write("\nPython")
    file.write("\nJava")
    file.write("\nC++")

# ==========================================================
# Create a New File
# ==========================================================

# Creates a new file.
# Raises FileExistsError if the file already exists.

with open("NewFile.txt", "x") as file:

    file.write("This is a new file.")

# ==========================================================
# Read and Write Mode
# ==========================================================

# Opens the file for both reading and writing.
# Writing starts from the current cursor position.

with open(fileName, "r+") as file:

    file.write("Hello")

# ==========================================================
# Write and Read Mode
# ==========================================================

# Deletes previous content before writing.

with open(fileName, "w+") as file:

    file.write("Fresh Data")

# ==========================================================
# Append and Read Mode
# ==========================================================

# Adds new data without deleting existing content.

with open(fileName, "a+") as file:

    file.write("\nMore Data")

# ==========================================================
# Write Binary File
# ==========================================================

binaryData = b"ABC123"

with open("Binary.bin", "wb") as file:

    file.write(binaryData)

# ==========================================================
# Flush Data Immediately
# ==========================================================

# Saves buffered data immediately.

with open(fileName, "w") as file:

    file.write("Python")

    file.flush()

# ==========================================================
# File Information
# ==========================================================

with open(fileName, "w") as file:

    file_name = file.name
    file_mode = file.mode
    can_write = file.writable()
    can_read = file.readable()
    is_closed = file.closed

closed_after = file.closed

# ==========================================================
# Write Using UTF-8 Encoding
# ==========================================================

with open(fileName, "w", encoding="utf-8") as file:

    file.write("السلام عليكم")

# ==========================================================
# Handle File Already Exists
# ==========================================================

try:

    with open("NewFile.txt", "x") as file:

        file.write("Python")

except FileExistsError:

    pass

# ==========================================================
# File Modes
# ==========================================================

# w   -> Write (Overwrite)
# a   -> Append
# x   -> Create New File
# r+  -> Read + Write
# w+  -> Write + Read
# a+  -> Append + Read
# wb  -> Write Binary

# ==========================================================
# Common Writing Methods
# ==========================================================

# file.write(text)
# file.writelines(list)
# file.flush()
# file.name
# file.mode
# file.closed
# file.readable()
# file.writable()


