def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sa = set(a)
    sb = set(b)

    if len(sa) + len(sb) < 4:
        print("NO")
    else:
        print("YES")

t = int(input())
for _ in range(t):
    solve()
