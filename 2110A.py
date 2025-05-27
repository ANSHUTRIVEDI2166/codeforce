def solve():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    
    if x[0] % 2 == x[-1] % 2:
        print(0)
        return
    
    left = n
    right = n
    
    for i in range(1, n):
        if x[i] % 2 != x[0] % 2:
            left = i
            break
    
    for i in range(1, n):
        if x[n - i - 1] % 2 != x[-1] % 2:
            right = i
            break
    
    print(min(left, right))

t = int(input())
for _ in range(t):
    solve()
