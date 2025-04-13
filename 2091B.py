def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    ans = 0
    cnt = 1
    for i in range(n):
        if a[i] * cnt >= x:
            ans += 1
            cnt = 0
        cnt += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()
