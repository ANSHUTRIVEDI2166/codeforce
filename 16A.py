def f(n, m, g):
    for i in range(n):
        if len(set(g[i])) > 1:
            return "NO"
        if i > 0 and g[i][0] == g[i - 1][0]:
            return "NO"
    return "YES"

n, m = map(int, input().split())
g = [input().strip() for _ in range(n)]
print(f(n, m, g))
