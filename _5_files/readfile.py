#fileName = "D:\\Python_journey\\_5_files\\Example1.txt"
fileName = r"D:\Python_journey\_5_files\Example1.txt"
# open(fileName,'r')
with open(fileName,'r') as file:
  filestuff= file.read()
  print(file.name)
  print(filestuff)
  file.closed



  #quick REVISION


# ----------------------------------------------------------
# Read only the first few characters
# ----------------------------------------------------------

with open(fileName, "r") as file:

    first10 = file.read(10)

# ----------------------------------------------------------
# Read one line at a time
# ----------------------------------------------------------

with open(fileName, "r") as file:

    line1 = file.readline()
    line2 = file.readline()

# ----------------------------------------------------------
# Read all lines into a list
# ----------------------------------------------------------

with open(fileName, "r") as file:

    lines = file.readlines()

# ----------------------------------------------------------
# Read the file using a loop
# (Best for large files)
# ----------------------------------------------------------

with open(fileName, "r") as file:

    for line in file:
        pass

# ----------------------------------------------------------
# File information
# ----------------------------------------------------------

with open(fileName, "r") as file:

    file_name = file.name
    file_mode = file.mode
    is_closed = file.closed
    can_read = file.readable()
    can_write = file.writable()

# File is automatically closed here

closed_after = file.closed

# ----------------------------------------------------------
# Current cursor position
# ----------------------------------------------------------

with open(fileName, "r") as file:

    position_before = file.tell()

    file.read(15)

    position_after = file.tell()

# ----------------------------------------------------------
# Move the cursor to another position
# ----------------------------------------------------------

with open(fileName, "r") as file:

    file.seek(20)

    data = file.read(10)

# ----------------------------------------------------------
# Read one character at a time
# ----------------------------------------------------------

with open(fileName, "r") as file:

    characters = []

    while True:

        ch = file.read(1)

        if not ch:
            break

        characters.append(ch)

# ----------------------------------------------------------
# Open a file with UTF-8 encoding
# ----------------------------------------------------------

with open(fileName, "r", encoding="utf-8") as file:

    text = file.read()

# ----------------------------------------------------------
# Handle missing files safely
# ----------------------------------------------------------

try:

    with open("Unknown.txt", "r") as file:

        data = file.read()

except FileNotFoundError:

    data = None

# ----------------------------------------------------------
# Read a binary file
# ----------------------------------------------------------

with open("image.jpg", "rb") as file:

    binary_data = file.read()

# ==========================================================
# Quick Revision
# ==========================================================

# open()         -> Open a file
# with           -> Automatically closes the file
# read()         -> Read the whole file
# read(n)        -> Read n characters
# readline()     -> Read one line
# readlines()    -> Read all lines into a list
# tell()         -> Current cursor position
# seek(pos)      -> Move the cursor
# readable()     -> Check if reading is allowed
# writable()     -> Check if writing is allowed
# closed         -> Check whether the file is closed
# name           -> File name or path
# mode           -> File opening mode

# ==========================================================
# File Modes
# ==========================================================

# r   -> Read text file
# rb  -> Read binary file

# ==========================================================
# Most Common Interview Methods
# ==========================================================

# file.read()
# file.read(10)
# file.readline()
# file.readlines()
# file.tell()
# file.seek()
# file.name
# file.mode
# file.closed
# file.readable()
# file.writable()
# with open(...)