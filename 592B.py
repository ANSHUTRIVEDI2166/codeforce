import math
n = int(input())

def solve(n):
    if n < 4:
        return 1
    else:
        n1 = (n-2)**2
        return n1

print(solve(n))
