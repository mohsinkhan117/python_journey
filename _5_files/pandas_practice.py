import pandas as pd

file1 = r"D:\Python_journey\_5_files\employees.csv"

df = pd.read_csv(filepath_or_buffer=file1)
print(df)

print(df.shape)      # (rows, columns)
print(df.columns)    # column names
df.info()            # already prints its own summary — no need to wrap in print()

# ----- Dictionary -> DataFrame -> CSV -----

# Correct shape: keys are COLUMN NAMES, values are the DATA for that column
dictData = {
    "name":   ["ali", "Mohsin khan"],
    "age":    [22, 22],
    "city":   ["bannu", "Peshawar"],
    "salary": [5000, 4000]
}

# Step 1: build the DataFrame from the dict
df2 = pd.DataFrame(dictData)
print(df2)

# Step 2: NOW save the DataFrame to CSV (index=False avoids writing row numbers)
df2.to_csv("dictData.csv", index=False)