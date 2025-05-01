def solve(n, x, k, s):
    i = 0
    ans = 0
    while i < n and k > 0:
        if s[i] == 'L':
            x -= 1
        else:
            x += 1
        k -= 1
        i += 1
        if x == 0:
            break

    if x == 0:
        ans = 1
        x = 0
        for j in range(n):
            if s[j] == 'L':
                x -= 1
            else:
                x += 1
            if x == 0:
                ans += k // (j + 1)
                break

    return ans

t = int(input())
for i in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    print(solve(n, x, k, s))
