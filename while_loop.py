
# 1. Counter - print 1 to 5
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print()  # Output: 1 2 3 4 5

# 2. Decrement - countdown from 5
i = 5
while i > 0:
    print(i, end=" ")
    i -= 1
print()  # Output: 5 4 3 2 1

# 3. Sum of first 10 numbers
sum = 0
i = 1
while i <= 10:
    sum += i
    i += 1
print(f"Sum: {sum}")  # Output: Sum: 55

# 4. Multiplication table of 5
i = 1
while i <= 10:
    print(f"5 x {i} = {5*i}")
    i += 1

# 5. Print even numbers 2 to 10
i = 2
while i <= 10:
    print(i, end=" ")
    i += 2
print()  # Output: 2 4 6 8 10


# Problem: Calculate sum of digits of 1234 (1+2+3+4=10)
num = 1234
sum_digits = 0
original = num

while num > 0:
    digit = num % 10  # Get last digit
    sum_digits += digit
    num = num // 10   # Remove last digit

print(f"Sum of digits of {original} is {sum_digits}")  # Output: 10


# check if number is palindrome
# Problem: Check if 12321 reads same backwards
num = 12321
original = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num = num // 10

if original == reversed_num:
    print(f"{original} is a palindrome")  # Output: 12321 is a palindrome
else:
    print(f"{original} is not a palindrome")