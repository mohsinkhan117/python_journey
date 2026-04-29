#factorial
def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(4))

#  Basic recursive Fibonacci 
def fib_basic(n):
    if n <= 1:
        return n
    return fib_basic(n-1) + fib_basic(n-2)

print("Basic Fibonacci:")
for i in range(10):
    print(fib_basic(i), end=" ")
print("\n")


#  Power function (exponentiation)
def power(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp-1)

print("2^10:", power(2, 10))
print("5^3:", power(5, 3))
print("2^-2:", power(2, -2))
print()


#  String reversal
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print("Reverse 'hello':", reverse_string("hello"))
print("Reverse 'python':", reverse_string("python"))
print()

# Palindrome check
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print("'racecar' palindrome:", is_palindrome("racecar"))
print("'hello' palindrome:", is_palindrome("hello"))
print("'A man a plan a canal panama' palindrome:", 
      is_palindrome("A man a plan a canal panama"))
print()