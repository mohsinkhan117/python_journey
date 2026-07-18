def isPallindrom( x):
    halfReversed =0
    while x>halfReversed:
        halfReversed= halfReversed*10+ (x%10)
        x/=10
    return (x == reversedHalf) or (x == reversedHalf / 10)
