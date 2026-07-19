from randomuser import RandomUser
import pandas as pd
import requests
import os

# ============================================================
# RANDOMUSER LIBRARY (pip install randomuser) — PANDAS, CSV, IMAGES
# This is a Python WRAPPER around the randomuser.me API - it hides
# all the raw requests.get()/JSON-parsing work behind clean getter
# methods, so you work with normal Python objects instead of dicts.
# ============================================================
#
# NOTE: this script makes REAL network calls, so run it on your
# own machine with internet access.
#   pip install randomuser pandas requests
#
# Library docs / source: https://pypi.org/project/randomuser/
# Underlying API docs:   https://randomuser.me/documentation
# ============================================================


print("\n================= GENERATING USERS =================")
# generate_users() is a STATIC method -> called on the class itself,
# not on an instance. Returns a LIST of RandomUser objects, one call,
# no manual loop needed (the library batches it into one API request).
users = RandomUser.generate_users(50)
print(type(users))
print(len(users))
print(type(users[0]))     # each item is a RandomUser OBJECT, not a raw dict

# You can also pass extra query parameters, same ones the raw API supports
# (nationality filter, gender filter, reproducible seed, etc.)
users_seeded = RandomUser.generate_users(10, {"seed": "revision123", "nat": "us,gb"})
print(len(users_seeded))

# -----------------------------------------------------------

print("\n================= GETTER METHODS ON A SINGLE USER =================")
# Every field is accessed through a get_...() method instead of dict keys -
# no risk of KeyError typos, and cleaner to read.
sample = users[0]

print(sample.get_full_name())      # "Jane Doe"
print(sample.get_gender())
print(sample.get_email())
print(sample.get_city())
print(sample.get_state())
print(sample.get_country())
print(sample.get_age())
print(sample.get_dob())            # raw ISO date string
print(sample.get_phone())
print(sample.get_cell())
print(sample.get_username())
print(sample.get_id())             # {'type': ..., 'number': ...}
print(sample.get_nat())            # nationality code, e.g. 'US'
print(sample.get_picture())        # large photo URL by default

# get_picture() accepts a size constant -> LARGE / MEDIUM / THUMBNAIL
print(sample.get_picture(RandomUser.PictureSize.THUMBNAIL))
print(sample.get_picture(RandomUser.PictureSize.MEDIUM))

# -----------------------------------------------------------

print("\n================= BUILDING A DATAFRAME FROM THE OBJECTS =================")
# Since users are OBJECTS (not raw JSON), there's no json_normalize() needed
# here - just call the getters in a loop/comprehension to build plain dicts,
# then hand that list of dicts straight to pandas.
rows = []
for user in users:
    rows.append({
        "full_name": user.get_full_name(),
        "gender": user.get_gender(),
        "email": user.get_email(),
        "city": user.get_city(),
        "state": user.get_state(),
        "country": user.get_country(),
        "age": user.get_age(),
        "date_of_birth": user.get_dob(),
        "phone": user.get_phone(),
        "nat": user.get_nat(),
        "photo_url": user.get_picture(),
        "thumbnail_url": user.get_picture(RandomUser.PictureSize.THUMBNAIL),
    })

df = pd.DataFrame(rows)
print(df.shape)
print(df.head())

# -----------------------------------------------------------

print("\n================= PARSING DATES =================")
df["date_of_birth"] = pd.to_datetime(df["date_of_birth"])
print(df["date_of_birth"].dtype)
print(df["date_of_birth"].dt.year.head())

# -----------------------------------------------------------

print("\n================= SAVING TO CSV =================")
df.to_csv("random_users_lib.csv", index=False)
print("Saved to random_users_lib.csv")

# -----------------------------------------------------------

print("\n================= READING THE CSV BACK =================")
df_loaded = pd.read_csv("random_users_lib.csv")
print(df_loaded.head())
print(df_loaded.dtypes)   # date_of_birth reverts to plain string after CSV round-trip
df_loaded["date_of_birth"] = pd.to_datetime(df_loaded["date_of_birth"])   # re-parse if needed

# -----------------------------------------------------------

print("\n================= FILTERING =================")
adults_over_30 = df[df["age"] > 30]
print(len(adults_over_30))

females = df[df["gender"] == "female"]
print(females[["full_name", "age", "country"]].head())

# -----------------------------------------------------------

print("\n================= SORTING =================")
df_sorted = df.sort_values("age", ascending=False)   # oldest first
print(df_sorted[["full_name", "age"]].head())

# -----------------------------------------------------------

print("\n================= GROUPING & AGGREGATING =================")
print(df.groupby("gender")["age"].mean())                          # average age per gender
print(df.groupby("country").size())                                  # users per country
print(df.groupby("gender")["age"].agg(["mean", "min", "max", "count"]))

# -----------------------------------------------------------

print("\n================= VALUE COUNTS =================")
print(df["gender"].value_counts())
print(df["country"].value_counts().head())

# -----------------------------------------------------------

print("\n================= SUMMARY STATISTICS =================")
print(df["age"].describe())
print(df["age"].mean())
print(df["age"].median())
print(df["age"].std())

# -----------------------------------------------------------

print("\n================= DOWNLOADING & SAVING PROFILE PICTURES =================")
# The library gives us the URL via get_picture() - downloading the actual
# bytes still needs requests, since that's outside what randomuser handles.
os.makedirs("profile_pictures", exist_ok=True)

for user in users[:5]:                              # just the first 5, to keep this quick
    img_response = requests.get(user.get_picture(), timeout=10)
    if img_response.status_code == 200:
        filename = f"profile_pictures/{user.get_full_name().replace(' ', '_')}.jpg"
        with open(filename, "wb") as f:              # "wb" -> write BINARY, since images aren't text
            f.write(img_response.content)
        print(f"Saved {filename}")
    else:
        print(f"Failed to download photo for {user.get_full_name()}")

# -----------------------------------------------------------

print("\n================= DISPLAYING A DOWNLOADED IMAGE =================")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

sample_image_path = f"profile_pictures/{users[0].get_full_name().replace(' ', '_')}.jpg"
if os.path.exists(sample_image_path):
    img = mpimg.imread(sample_image_path)
    plt.imshow(img)
    plt.axis("off")
    plt.title(users[0].get_full_name())
    plt.savefig("sample_profile_preview.png")   # saved to a file so it works in any environment
    print("Preview saved as sample_profile_preview.png")
    # plt.show()   # uncomment locally for an interactive pop-up window instead

# -----------------------------------------------------------

print("\n================= EXPORTING A FILTERED SUBSET =================")
df[df["age"] < 30][["full_name", "age", "country", "email"]].to_csv(
    "young_users_subset.csv", index=False
)
print("Saved filtered subset to young_users_subset.csv")

# -----------------------------------------------------------

print("\n================= LIBRARY (randomuser) vs RAW requests+JSON =================")
#   TASK                              randomuser LIBRARY                    RAW requests + JSON
#   ---------------------------------  -------------------------------------  ---------------------------------------
#   Fetch multiple users                RandomUser.generate_users(50)           requests.get(url, params={"results":50})
#   Access a field                       user.get_full_name()                     data["results"][0]["name"]["first"] + ...
#   Risk of typos/KeyError                 low (methods, IDE autocomplete)          higher (raw dict key strings)
#   Flatten into DataFrame                  loop + getters -> list of dicts           pd.json_normalize(data["results"])
#   Extra query params (seed, nat, etc)      generate_users(n, {"seed": ...})           requests.get(url, params={...})
#   Best for                                 quick, readable, beginner-friendly code    full control / advanced API features

# -----------------------------------------------------------

print("\n================= QUICK REFERENCE: KEY GETTER METHODS =================")
#   GETTER METHOD                 RETURNS
#   -----------------------------  --------------------------------------------
#   get_full_name()                 "First Last" string
#   get_gender()                     'male' / 'female'
#   get_email()                       email address
#   get_city() / get_state() / get_country()   location fields
#   get_age() / get_dob()               age (int) / date of birth (ISO string)
#   get_phone() / get_cell()             contact numbers
#   get_username()                        login username
#   get_id()                               {'type': ..., 'number': ...}
#   get_nat()                               nationality code (e.g. 'US')
#   get_picture(size=...)                    photo URL - LARGE / MEDIUM / THUMBNAIL