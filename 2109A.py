def solve():
    n = int(input())
    a = list(map(int, input().split()))

    if sum(a) == n:
        print("YES")
        return

    for i in range(n - 1):
        if a[i] == 0 and a[i + 1] == 0:
            print("YES")
            return

    print("NO")

t = int(input())
for _ in range(t):
    solve()
