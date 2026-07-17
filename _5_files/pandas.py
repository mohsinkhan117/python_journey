import pandas as pd

# ============================================================
# PANDAS — QUICK REVISION SHEET
# Covers: opening a CSV, formatting a dataframe, adding data,
# slicing a dataframe, and loc[] vs iloc[]
# ============================================================


print("\n================= OPENING A CSV =================")
# read_csv() -> loads a CSV file into a DataFrame (a table-like structure)
df = pd.read_csv("employees.csv")
print(df)

# -----------------------------------------------------------

print("\n================= BASIC INSPECTION =================")
# Quick ways to understand a dataframe before working with it
print(df.head())      # first 5 rows (default) -> good for a quick peek
print(df.tail(2))     # last 2 rows
print(df.shape)       # (rows, columns) -> size of the dataframe
print(df.columns)     # list of column names
print(df.dtypes)      # data type of each column (int, object/str, float...)
print(df.info())      # summary: columns, non-null counts, dtypes, memory

# -----------------------------------------------------------

print("\n================= CSV FORMATTING (read_csv OPTIONS) =================")
# read_csv() has many parameters to control HOW the file is parsed

# use a specific column as the row index instead of default 0,1,2...
df_indexed = pd.read_csv("employees.csv", index_col="name")
print(df_indexed)

# rename columns while reading (or after, using df.columns / df.rename)
df_renamed = df.rename(columns={"salary": "monthly_salary"})
print(df_renamed)

# selecting only certain columns while reading -> saves memory on big files
df_partial = pd.read_csv("employees.csv", usecols=["name", "city"])
print(df_partial)

# controlling dtype explicitly (useful when pandas guesses wrong)
df_typed = pd.read_csv("employees.csv", dtype={"age": "int32"})
print(df_typed.dtypes)

# -----------------------------------------------------------

print("\n================= HEADER ROW BEHAVIOR (header=) =================")
# By default, read_csv() assumes the FIRST row is the header (header=0).
# This isn't magic detection - it's just pandas' default assumption,
# and you can override it whenever your file doesn't follow that pattern.

# Default behavior -> row 0 becomes column names automatically
df_default = pd.read_csv("employees.csv")
print(df_default.columns.tolist())     # ['name', 'age', 'city', 'salary']

# header=None -> no header row exists in the file at all
# pandas then auto-generates column names: 0, 1, 2, 3...
df_no_header = pd.read_csv("employees.csv", header=None)
print(df_no_header.head(2))            # first row is now treated as DATA, not column names

# header=1 -> use row 2 (0-indexed as 1) as the header instead of row 1
# useful when a file has junk/metadata on the very first line
# df_header_row2 = pd.read_csv("some_file.csv", header=1)

# Supplying your OWN column names (ignores whatever the file's first row says)
df_custom_names = pd.read_csv("employees.csv", header=0, names=["emp_name", "emp_age", "emp_city", "emp_salary"])
print(df_custom_names.head(2))

# -----------------------------------------------------------

print("\n================= WRITING / SAVING A CSV =================")
# to_csv() -> opposite of read_csv(), saves a dataframe back to a file
df.to_csv("employees_copy.csv", index=False)   # index=False -> don't write row numbers
print("Saved to employees_copy.csv")

# -----------------------------------------------------------

print("\n================= ADDING DATA: NEW COLUMN =================")
# Adding a column is as simple as assigning to a new column name
df["bonus"] = df["salary"] * 0.10          # calculated column based on existing data
print(df)

# Adding a column with a fixed/default value for every row
df["department"] = "General"
print(df)

# -----------------------------------------------------------

print("\n================= ADDING DATA: NEW ROW =================")
# Method 1: pd.concat() -> append a new row (as a small dataframe) to df
new_row = pd.DataFrame([{
    "name": "Hina", "age": 24, "city": "Quetta",
    "salary": 48000, "bonus": 4800, "department": "General"
}])
df = pd.concat([df, new_row], ignore_index=True)   # ignore_index -> re-numbers rows cleanly
print(df)

# Method 2: df.loc[new_index] -> directly insert a row at a chosen index label
df.loc[len(df)] = ["Zara", 26, "Sialkot", 52000, 5200, "General"]
print(df)

# -----------------------------------------------------------

print("\n================= SLICING A DATAFRAME =================")
# Slicing with [] on a dataframe works similarly to lists, but on ROWS by default
print(df[0:3])          # first 3 rows (rows 0, 1, 2) -> like list slicing

# Selecting a single column -> returns a Series (1D)
print(df["name"])

# Selecting multiple columns -> pass a list of column names, returns a DataFrame
print(df[["name", "salary"]])

# Filtering rows with a condition (boolean mask) -> very common in real use
print(df[df["age"] > 25])                 # only rows where age > 25
print(df[(df["age"] > 25) & (df["salary"] > 50000)])   # combine conditions with & / |

# -----------------------------------------------------------

print("\n================= loc[] — LABEL-BASED SELECTION =================")
# loc[] selects by LABEL (row index label / column name), NOT position
# Syntax: df.loc[row_label, column_label]

print(df.loc[0])                       # row with index label 0 (all columns)
print(df.loc[0, "name"])               # single value -> name at row label 0
print(df.loc[0:2, "name"])             # rows 0 to 2 INCLUSIVE (unlike normal slicing!)
print(df.loc[0:2, ["name", "city"]])   # multiple rows + specific columns
print(df.loc[df["age"] > 25, "name"])  # condition-based filtering, only 'name' column

# -----------------------------------------------------------

print("\n================= iloc[] — POSITION-BASED SELECTION =================")
# iloc[] selects by INTEGER POSITION only, regardless of index labels
# Syntax: df.iloc[row_position, column_position]

print(df.iloc[0])              # first row by position
print(df.iloc[0, 0])           # value at row 0, column 0 (position-based)
print(df.iloc[0:2])            # first 2 rows -> stop is EXCLUSIVE (normal Python slicing rules)
print(df.iloc[0:2, 0:2])       # first 2 rows, first 2 columns
print(df.iloc[-1])             # last row -> negative indexing works like lists
print(df.iloc[[0, 2, 4]])      # specific rows by position (list of positions)

# -----------------------------------------------------------

print("\n================= loc[] vs iloc[] — QUICK COMPARISON =================")
#   FEATURE                 loc[]                          iloc[]
#   ----------------------  -----------------------------  -----------------------------
#   Selection basis           LABEL (index/column name)       POSITION (integer, 0-based)
#   Slice end behavior         INCLUSIVE of the end label        EXCLUSIVE of the end position
#   Works with conditions       Yes (boolean masks)               No (position only)
#   Works with negative index    No (unless label is negative)     Yes (like list[-1])