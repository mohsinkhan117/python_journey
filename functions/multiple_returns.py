
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(minimum, maximum)


def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide(17, 5)
print(q, r)   # 3 2


def separate_even_odd(nums):
   
    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 != 0]
    return evens, odds

e, o = separate_even_odd([1, 2, 3, 4, 5, 6])
print(e, o)