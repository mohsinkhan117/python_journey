"""
You don’t declare variables separately like in C/C++/Java.
Python uses dynamic typing, so a variable is created the moment you assign a value. so we don't need to declare just 
variables, everything is done in a go
"""
a = None   # placeholder (represents "no value")


x = 10        # int
y = 3.14      # float
z = "Hello"   # string
multi_line = """This is
a multi-line
string"""
flag = True   # boolean
c = 2 + 3j    # complex

lst = [1, 2, 3]     # list (mutable)
print(len(lst))
print(max(lst))
print(min(lst))
print(sum(lst))

tup = (1, 2, 3)     # tuple (immutable)

s1 = {1, 2, 3}      # set
s2 = frozenset([1,2,3])  # immutable set

d = {"name": "Mohsin", "age": 20}   # dictionary

p, q, r = 1, 2, 3
print(p, q, r)

u = v = w = 0
print(u, v, w)

name="Mohsin_khan"
print(len(name))
print(name.upper())
print(name.lower())
print(name.replace("_", " "))

print(type(a))
print(type(x))
print(type(y))
print(type(z))
print(type(flag))
print(type(c))
print(type(lst))
print(type(tup))
print(type(s1),"sets")
print(type(s2),"frozen sets")

print(name)
#how can we just declare the varibles 
#give me list of all types of variables in python


#unicode vs char
#ord converts to unicode and where as chr converts to real charater 

char_a = 'a'
unicode_a = ord(char_a)
print("unicode of a is: ",unicode_a)

print("char of a unicode of a is: ", chr(unicode_a))


#type casting 
print("------ type casting ---------")

string_a = str(a)
int_from_str = int("100")
float_from_str = float("3.5")
bool_from_int = bool(1)

print(type(int_from_str), int_from_str)
print(type(float_from_str), float_from_str)
print(type(bool_from_int), bool_from_int)


#user input  
user_input = input("Enter a number/string/ anything but in formatted form: ")
print("You have entered:", user_input)