def solve():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        b = [0] * n
        b[0] = a[0]
        for i in range(1, n):
            b[i] = max(b[i-1], a[i])

        c = [0] * (n + 1)
        for i in range(1, n+1):
            c[i] = c[i-1] + a[n-i]

        d = []
        for k in range(1, n+1):
            e = c[k]
            if n - k > 0:
                e = max(e, b[n-k-1] + c[k-1])
            d.append(e)

        print(*d)


solve()
