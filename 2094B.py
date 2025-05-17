def solve():
    n, m, l, r = map(int, input().split())
    diff = n - m
    l = abs(l)
    
    if l >= diff:
        l -= diff
        diff = 0
    else:
        diff -= l
        l = 0
    
    print(-l, r - diff)

t = int(input())
for _ in range(t):
    solve()
