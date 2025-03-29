import math

y, w = map(int, input().split())
m = max(y, w)
numerator = 7 - m
denominator = 6
g = math.gcd(numerator, denominator)
numerator //= g
denominator //= g
print(f"{numerator}/{denominator}")
