t = int(input())
for i in range(t):
    n, m, r, c = map(int, input().split())
    i = (r - 1) * m + c
    total = m * (n - r) + n * m - i - (n - r)
    print(total)
