def f(n, m, g):
    t, b = n, 0
    l, r = m, 0

    for i in range(n):
        for j in range(m):
            if g[i][j] == '*':
                t = min(t, i)
                b = max(b, i)
                l = min(l, j)
                r = max(r, j)

    for i in range(t, b + 1):
        print(g[i][l:r + 1])

n, m = map(int, input().split())
g = [input().strip() for _ in range(n)]
f(n, m, g)
