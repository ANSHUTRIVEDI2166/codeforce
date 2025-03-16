import sys
import math
from collections import deque
 
def is_perfect_square(x):
    if x < 0:
        return False
    r = int(math.sqrt(x))
    return r * r == x
 
def anshu_solver():
    n = int(sys.stdin.readline().strip())
    total_sum = n * (n + 1) // 2
 
    if is_perfect_square(total_sum):
        print("-1")
        return
 
    rem = deque(range(n, 0, -1))
    pr_su = 0
    perm = []
 
    while rem:
        for i in range(len(rem)):  
            val = rem[i]
            if not is_perfect_square(pr_su + val):
                perm.append(val)
                pr_su += val
                rem.remove(val) 
                break
 
    print(*perm)
 
t = int(sys.stdin.readline().strip())
for _ in range(t):
    anshu_solver()
