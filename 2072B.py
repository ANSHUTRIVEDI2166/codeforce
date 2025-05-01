def solve(s, n):
    c = 0
    ans = 0
    if n < 2:
        return 0
    for j in range(n):
        if s[j] == '-':
            c += 1
    ans = (c // 2) * (c - c // 2) * (n - c)
    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(s, n))
