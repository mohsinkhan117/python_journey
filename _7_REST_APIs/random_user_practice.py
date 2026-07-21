from randomuser import RandomUser
import pandas as pd

users= RandomUser.generate_users(10)
print(users)


userlist=[]
for user in users:
   userlist.append(
      {"full_name": user.get_full_name(),
        "gender": user.get_gender(),
        "email": user.get_email(),
        "city": user.get_city(),
        "state": user.get_state(),
        "country": user.get_country(),
        "age": user.get_age(),
        "date_of_birth": user.get_dob(),
        "phone": user.get_phone(),
        "nat": user.get_nat(),
        "photo_url": user.get_picture(),}
   )


df= pd.DataFrame(userlist)
print(f"DataFrame:\n{df}\n")

df.to_csv("usersFile")

