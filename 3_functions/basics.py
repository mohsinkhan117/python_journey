def hello():
    print('This is hello function')


hello()

def greet_user(name):
    print(f"Hello, {name}")

greet_user("Mohsin")


def sum(a,b):
    return a+b

print('sum of a and b is: ',sum(3,5))

def exp(base,exp=2): # bydefault set to 2
    return base **exp

print("exponentially 4 and 2 is ",exp(4))
print("exponentially 3 and 3 is ",exp(3,3))


#arguments are interchangeable by using the keyword
def student(name, age):
    print(name, age)

student(age=20, name="Ali")



#arbitrary numbers of arguments 

def total_sum(*numbers):
    return sum(numbers)

print(total_sum(1, 2, 3, 4, 5))



#nested functions
def f1():
    s = 'I love python'
    def f2():
        print(s)
        
    f2()
f1()