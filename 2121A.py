t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    x = list(map(int, input().split()))
    L = x[0]
    R = x[-1]
    
    if s <= L:
        steps = R - s
    elif s >= R:
        steps = s - L
    else:
        steps = (R - L) + min(s - L, R - s)
    
    print(steps)
