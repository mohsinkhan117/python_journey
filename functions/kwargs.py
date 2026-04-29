def create_user(**user_data):
    for key,value in user_data.items():
         print(f"{key}: {value}", end='\n')


create_user(Name='Mohsin khan', age=22, city='Peshawar')

# the kwargs are handled internally without using loops
def create_user(**kwargs):
    return kwargs

user = create_user(name="Mohsin", age=22, city="Peshawar")
print(user)





#real world connection
def connect_db(**config):
    host = config.get("host", "localhost")
    port = config.get("port", 3306)
    print(f"Connecting to {host}:{port}")

connect_db(host="127.0.0.1")



#internally handled 
data = {"x": 10, "y": 20}

def point(x, y):
    print(x, y)

point(**data)