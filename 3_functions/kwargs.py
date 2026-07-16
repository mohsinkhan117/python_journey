'''
*args: collects extra positional (non-keyword) arguments as a tuple.
**kwargs: collects extra keyword arguments as a dictionary.
'''

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


def student_info(*args, **kwargs):
    print("Subjects:", args)        # Positional arguments
    print("Details:", kwargs)       # Keyword arguments

# Passing subjects as *args and details as **kwargs
student_info("Math", "Science", "English", Name="Alice", Age=20, City="New York")




def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')