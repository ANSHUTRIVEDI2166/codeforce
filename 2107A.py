t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    mn = min(a)
    mx = max(a)
    
    if mn == mx:
        print("No")
        continue
    
    print("Yes")
    result = [1 + (x == mx) for x in a]
    print(*result)
